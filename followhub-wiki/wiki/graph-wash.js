// @ts-nocheck
/* ============================================================
   Knowledge Graph runtime
   ============================================================ */
(async function () {
  "use strict";

  const helpers = window.WikiGraphWashHelpers;
  if (!helpers) {
    console.error("[wiki] graph-wash-helpers.js is missing or failed to load");
    return;
  }

  const {
    createSafeStorage,
    getWikiStorageNamespace,
    defaultQueue,
    normalizeQueue,
    toggleQueueFavorite,
    appendQueueNote,
    summarizeQueue,
    buildAtlasModel,
    deriveAtlasLayout,
    resolveAtlasVisibleSnapshot,
    resolveAtlasSelectedNodeId,
    atlasNodePoint,
    getAtlasModelBounds,
    fitAtlasViewport,
    centerAtlasViewportOnPoint,
    zoomAtlasViewport,
    atlasViewportToMinimapRect,
    atlasPointToMinimap,
    minimapPointToAtlasPoint,
    atlasConfidenceLabel,
    atlasTypeLabel,
    atlasNodeKind,
    stripAtlasMarkdown
  } = helpers;

  const DENSITY_SMALL_LIMIT = 80;
  const DENSITY_MEDIUM_LIMIT = 200;
  const DENSITY_LARGE_LIMIT = 500;
  const QUEUE_NOTE_LIMIT = 50;
  const NOTE_EXCERPT_LIMIT = 140;
  const TOPIC_PAGE_SIZE = 8;
  const COMMUNITY_COLORS = ["#2563eb", "#334155", "#0f766e", "#b45309", "#7c3aed", "#15803d", "#64748b", "#475569"];

  let dataError = false;

  async function loadGraphData() {
    const dataUrl = window.WIKI_GRAPH_DATA_URL;
    if (dataUrl) {
      try {
        const response = await fetch(dataUrl, { headers: { accept: "application/json" } });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return await response.json();
      } catch (err) {
        console.error("[wiki] graph data fetch failed:", err);
        dataError = true;
      }
    }

    const dataEl = document.getElementById("graph-data");
    try {
      return dataEl ? JSON.parse(dataEl.textContent) : window.SAMPLE_GRAPH;
    } catch (err) {
      console.error("[wiki] graph data parse failed:", err);
      dataError = true;
      return { meta: {}, nodes: [], edges: [], insights: { meta: { degraded: true } } };
    }
  }

  const DATA = await loadGraphData();

  const app = document.getElementById("app");
  const atlas = document.getElementById("atlas");
  const nodeLayer = document.getElementById("node-layer");
  const edgeLayer = document.getElementById("edge-layer");
  const synthesisList = document.getElementById("synthesis-list");
  const topicList = document.getElementById("topic-list");
  const papersIndex = document.getElementById("papers-index");
  const papersMain = document.getElementById("papers-main");
  const papersSearch = document.getElementById("papers-search");
  const papersSort = document.getElementById("papers-sort");
  const readerArticle = document.getElementById("reader-article");
  const readerTitle = document.getElementById("reader-title");
  const readerSubtitle = document.getElementById("reader-subtitle");
  const searchInput = document.getElementById("search");
  const noResults = document.getElementById("no-results");
  const canvasTitle = document.getElementById("canvas-title");
  const canvasSubtitle = document.getElementById("canvas-subtitle");
  const insightTitle = document.getElementById("insight-title");
  const insightCopy = document.getElementById("insight-copy");
  const drawer = document.getElementById("drawer");
  const drawerNeighbors = document.getElementById("neighbor-details");
  const drawerNeighborsHeading = drawerNeighbors ? drawerNeighbors.querySelector("summary") : null;
  const neighborList = document.getElementById("neighbor-list");
  const minimapEl = document.getElementById("minimap");
  const minimapToggle = document.getElementById("minimap-toggle");
  const minimapSvg = document.getElementById("mini-map-svg");

  if (!atlas || !nodeLayer || !edgeLayer) {
    console.error("[wiki] atlas shell is incomplete");
    return;
  }

  let rawLocalStorage = null;
  try {
    rawLocalStorage = window.localStorage;
  } catch (_) {}

  const atlasModel = buildAtlasModel(DATA);
  const atlasLayout = deriveAtlasLayout(atlasModel);
  const safeLocalStorage = createSafeStorage(rawLocalStorage, console.warn);
  const storageNamespace = getWikiStorageNamespace(atlasModel.meta, window.location && window.location.pathname);

  const state = {
    atlasModel,
    atlasLayout,
    queue: loadQueueState(),
    ui: {
      selectedNodeId: null,
      route: "graph",
      papersQuery: "",
      papersSort: "date-desc",
      activeCommunityId: "all",
      focusMode: "all",
      scopedNodeId: null,
      topicPage: 0,
      query: "",
      dimUnselected: false,
      dataMode: dataError ? "error" : (atlasModel.nodes.length ? "normal" : "empty"),
      neighborExpanded: false,
      filters: { EXTRACTED: true, INFERRED: true, AMBIGUOUS: true, UNVERIFIED: true }
    },
    viewport: { x: 0, y: 0, scale: 1 },
    viewportReady: false,
    visible: null
  };

  let viewportPaintFrame = 0;
  let panState = null;

  function queueStorageKey(name) {
    return storageNamespace + ":" + name;
  }

  function loadQueueState() {
    const raw = safeLocalStorage.get(queueStorageKey("queue"));
    if (!raw) return defaultQueue();
    try {
      return normalizeQueue(JSON.parse(raw));
    } catch (err) {
      console.warn("[wiki] queue storage parse failed:", err);
      return defaultQueue();
    }
  }

  function persistQueueState() {
    safeLocalStorage.set(queueStorageKey("queue"), JSON.stringify(state.queue));
  }

  function escapeHtml(value) {
    return String(value == null ? "" : value).replace(/[&<>"']/g, (ch) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;"
    })[ch]);
  }

  function clampWeight(value) {
    const numeric = Number(value);
    if (!Number.isFinite(numeric)) return 0.6;
    return Math.max(0, Math.min(1, numeric));
  }

  function edgeStrokeWidth(edge) {
    return 1.1 + clampWeight(edge && edge.weight) * 1.8;
  }

  function edgeOpacity(edge) {
    return 0.32 + clampWeight(edge && edge.weight) * 0.44;
  }

  function edgeStrengthSize(edge) {
    return 6 + clampWeight(edge && edge.weight) * 8;
  }

  function currentDensityMode() {
    return state.visible ? state.visible.densityMode : "card";
  }

  function communityColor(communityId) {
    const community = state.atlasModel.communityById[communityId];
    const index = community ? community.color_index || 0 : 0;
    return COMMUNITY_COLORS[index % COMMUNITY_COLORS.length];
  }

  function getSelectedNode() {
    const selectedNodeId = resolveAtlasSelectedNodeId(state.atlasModel, state.visible, state.ui.selectedNodeId);
    return selectedNodeId ? state.atlasModel.byId[selectedNodeId] || null : null;
  }

  function getPreviewStartEntry(visibleSnapshot) {
    if (state.ui.selectedNodeId) return null;
    const visible = visibleSnapshot || state.visible || refreshVisibleSnapshot();
    const visibleIds = new Set((visible.node_ids || []).map(String));
    const starts = visible.starts && visible.starts.length
      ? visible.starts
      : state.atlasModel.starts.filter((entry) => entry && entry.node && visibleIds.has(entry.node.id));
    if (starts.length) return starts[0];
    const fallback = (visible.nodes || []).slice().filter((node) => {
      return node && (node.summary || node.content || node.source_path);
    }).sort((left, right) => (right.priority || 0) - (left.priority || 0))[0];
    return fallback ? { node: fallback, reason: "当前范围 · 推荐预览" } : null;
  }

  function refreshVisibleSnapshot() {
    state.visible = resolveAtlasVisibleSnapshot(state.atlasModel, state.atlasLayout, state.ui);
    state.ui.selectedNodeId = resolveAtlasSelectedNodeId(state.atlasModel, state.visible, state.ui.selectedNodeId);
    return state.visible;
  }

  function currentViewportSize() {
    const rect = atlas.getBoundingClientRect();
    return {
      width: rect && rect.width ? rect.width : 1000,
      height: rect && rect.height ? rect.height : 680
    };
  }

  function viewportOptions() {
    return { minScale: 0.62, maxScale: 3.2 };
  }

  function edgeTransformForViewport(viewport, size) {
    const safeSize = size || currentViewportSize();
    const x = (viewport.x / safeSize.width) * 1000;
    const y = (viewport.y / safeSize.height) * 680;
    return `translate(${x} ${y}) scale(${viewport.scale})`;
  }

  function applyViewportTransform() {
    const size = currentViewportSize();
    if (nodeLayer) {
      nodeLayer.style.transform = `translate(${state.viewport.x}px, ${state.viewport.y}px) scale(${state.viewport.scale})`;
    }
    if (edgeLayer) {
      edgeLayer.setAttribute("transform", edgeTransformForViewport(state.viewport, size));
    }
    updateMinimapViewport();
  }

  function updateMinimapViewport() {
    if (!minimapSvg) return;
    const rect = minimapSvg.querySelector(".mini-map-viewport");
    if (!rect) return;
    const miniRect = atlasViewportToMinimapRect(state.viewport, currentViewportSize());
    rect.setAttribute("x", String(miniRect.x));
    rect.setAttribute("y", String(miniRect.y));
    rect.setAttribute("width", String(miniRect.width));
    rect.setAttribute("height", String(miniRect.height));
  }

  function scheduleViewportPaint() {
    if (viewportPaintFrame) return;
    viewportPaintFrame = window.requestAnimationFrame(() => {
      viewportPaintFrame = 0;
      applyViewportTransform();
    });
  }

  function setViewport(nextViewport, immediate) {
    state.viewport = helpers.clampAtlasViewport(nextViewport, currentViewportSize(), viewportOptions());
    if (immediate) {
      if (viewportPaintFrame) {
        window.cancelAnimationFrame(viewportPaintFrame);
        viewportPaintFrame = 0;
      }
      applyViewportTransform();
    } else {
      scheduleViewportPaint();
    }
  }

  function fitVisibleViewport() {
    const visible = state.visible || refreshVisibleSnapshot();
    const bounds = getAtlasModelBounds(visible.nodes, visible.nodes.length <= 1 ? 160 : 56);
    setViewport(fitAtlasViewport(bounds, currentViewportSize(), { padding: 0.82, minScale: 0.62, maxScale: 1.18 }), true);
    state.viewportReady = true;
  }

  function centerViewportOnNode(nodeId) {
    const node = state.atlasModel.byId[nodeId];
    if (!node) return;
    const scale = Math.max(1.05, Math.min(state.viewport.scale || 1, 1.6));
    setViewport(centerAtlasViewportOnPoint(atlasNodePoint(node), currentViewportSize(), scale, viewportOptions()), true);
    state.viewportReady = true;
  }

  function makePath(a, b, edge) {
    const sourcePoint = atlasNodePoint(a);
    const targetPoint = atlasNodePoint(b);
    const x1 = sourcePoint.x;
    const y1 = sourcePoint.y;
    const x2 = targetPoint.x;
    const y2 = targetPoint.y;
    const mx = (x1 + x2) / 2;
    const my = (y1 + y2) / 2;
    const curve = Math.max(-76, Math.min(76, (a.y - b.y) * 1.8 + (clampWeight(edge.weight) - 0.5) * 24));
    return `M ${x1} ${y1} Q ${mx + curve} ${my - 22} ${x2} ${y2}`;
  }

  function edgeClass(edge) {
    return String(edge.type || "EXTRACTED").toLowerCase();
  }

  function connectedIds(id) {
    const out = new Set([id]);
    state.atlasModel.edges.forEach((edge) => {
      if (edge.source === id) out.add(edge.target);
      if (edge.target === id) out.add(edge.source);
    });
    return out;
  }

  function nodeNeighborCount(id) {
    return Math.max(0, connectedIds(id).size - 1);
  }

  function nodeMetaLabel(node) {
    if (node.unavailable) return "材料暂不可用";
    const count = nodeNeighborCount(node.id);
    if (count === 0) return "孤立节点";
    if (count >= 3) return `${count} 个关联 · 关键连接`;
    return `${count} 个关联`;
  }

  function isNodeImportant(node) {
    return !!(node && state.visible && state.visible.importantNodeIds && state.visible.importantNodeIds[node.id]);
  }

  function nodeVisualRole(node, displayMode, previewNodeId) {
    if (!node) return "landmark";
    if (node.id === state.ui.selectedNodeId) return "cinnabar-note";
    if (displayMode === "point" || displayMode === "overview") return "map-pin";
    if (state.visible && state.visible.matchedNodeIds[node.id]) return "index-slip";
    if (previewNodeId && node.id === previewNodeId) return "index-slip";
    if (isNodeImportant(node)) return "index-slip";
    return "landmark";
  }

  function nodeDisplayMode(node, previewNodeId) {
    const mode = currentDensityMode();
    if (!node) return "card";
    if (node.id === state.ui.selectedNodeId) return "card";
    if (state.visible && state.visible.matchedNodeIds[node.id]) return "card";
    if (previewNodeId && node.id === previewNodeId && (mode === "overview" || mode === "point-plus-focus")) return "compact-card";
    if (isNodeImportant(node) && (mode === "overview" || mode === "point-plus-focus")) return "compact-card";
    if (mode === "overview") return state.visible.labelNodeIds[node.id] ? "compact-card" : "overview";
    if (mode === "point-plus-focus") return state.visible.labelNodeIds[node.id] ? "compact-card" : "point";
    return mode;
  }

  function renderTopbar() {
    const title = document.getElementById("wiki-title");
    if (title) title.textContent = state.atlasModel.meta.wiki_title || "知识图谱";
  }

  function nodesByType(type) {
    return state.atlasModel.nodes
      .filter((node) => node.type === type)
      .slice()
      .sort((left, right) => {
        const leftDate = Date.parse(left.publish_date || "") || 0;
        const rightDate = Date.parse(right.publish_date || "") || 0;
        if (leftDate !== rightDate) return rightDate - leftDate;
        if ((right.priority || 0) !== (left.priority || 0)) return (right.priority || 0) - (left.priority || 0);
        return String(left.label || "").localeCompare(String(right.label || ""), "zh-Hans-CN");
      });
  }

  function focusSidebarNode(node) {
    if (node && (node.type === "topic" || node.type === "synthesis")) {
      state.ui.scopedNodeId = node.id;
      state.ui.focusMode = "all";
      document.querySelectorAll("[data-focus]").forEach((item) => {
        item.setAttribute("aria-pressed", item.dataset.focus === "all" ? "true" : "false");
      });
    }
    focusNode(node.id, true);
  }

  function renderNodeList(list, nodes, emptyText) {
    if (!list) return;
    list.innerHTML = "";
    nodes.forEach((node) => {
      const card = document.createElement("div");
      card.className = "start-card";
      card.dataset.nodeType = node.type;
      card.dataset.selected = state.ui.selectedNodeId === node.id ? "true" : "false";
      card.innerHTML = `
        <button class="start-card__main" type="button">
          <span class="card-copy"><strong>${escapeHtml(node.label)}</strong><span>${escapeHtml(node.publish_date || atlasTypeLabel(node.type))}</span></span>
        </button>
        <a class="start-card__link" href="${escapeHtml(nodeWikiUrl(node))}" target="_top">打开</a>
      `;
      const locate = card.querySelector(".start-card__main");
      if (locate) locate.addEventListener("click", () => focusSidebarNode(node));
      list.appendChild(card);
    });
    if (!list.children.length) {
      const empty = document.createElement("div");
      empty.className = "note-card";
      empty.textContent = emptyText;
      list.appendChild(empty);
    }
  }

  function renderTopicList() {
    if (!topicList) return;
    const topics = nodesByType("topic");
    const pageCount = Math.max(1, Math.ceil(topics.length / TOPIC_PAGE_SIZE));
    state.ui.topicPage = Math.max(0, Math.min(state.ui.topicPage || 0, pageCount - 1));
    const start = state.ui.topicPage * TOPIC_PAGE_SIZE;
    renderNodeList(topicList, topics.slice(start, start + TOPIC_PAGE_SIZE), "暂无主题节点。");
    if (pageCount <= 1 || !topicList.children.length) return;

    const pager = document.createElement("div");
    pager.className = "list-pager";
    pager.innerHTML = `
      <button type="button" ${state.ui.topicPage === 0 ? "disabled" : ""}>上一页</button>
      <span>${state.ui.topicPage + 1} / ${pageCount}</span>
      <button type="button" ${state.ui.topicPage >= pageCount - 1 ? "disabled" : ""}>下一页</button>
    `;
    const buttons = pager.querySelectorAll("button");
    if (buttons[0]) {
      buttons[0].addEventListener("click", () => {
        state.ui.topicPage = Math.max(0, state.ui.topicPage - 1);
        renderSidebar();
      });
    }
    if (buttons[1]) {
      buttons[1].addEventListener("click", () => {
        state.ui.topicPage = Math.min(pageCount - 1, state.ui.topicPage + 1);
        renderSidebar();
      });
    }
    topicList.appendChild(pager);
  }

  function renderSidebar() {
    renderNodeList(synthesisList, nodesByType("synthesis"), "暂无综述节点。");
    renderTopicList();
  }

  function sourceNodesSorted() {
    let nodes = state.atlasModel.nodes
      .filter((node) => node.type === "source")
      .slice();

    if (state.ui.papersQuery) {
      const q = state.ui.papersQuery.toLowerCase();
      nodes = nodes.filter((node) => {
        const hay = [node.label, node.summary, node.content, (node.keywords || []).join(" ")].join(" ").toLowerCase();
        return hay.includes(q);
      });
    }

    nodes.sort((left, right) => {
      if (state.ui.papersSort === "title-asc") {
        return String(left.label || "").localeCompare(String(right.label || ""), "zh-Hans-CN");
      }
      const leftDate = Date.parse(left.publish_date || "") || 0;
      const rightDate = Date.parse(right.publish_date || "") || 0;
      if (state.ui.papersSort === "date-asc") {
        if (leftDate !== rightDate) return leftDate - rightDate;
      } else {
        const leftDate = Date.parse(left.publish_date || "") || 0;
        const rightDate = Date.parse(right.publish_date || "") || 0;
        if (leftDate !== rightDate) return rightDate - leftDate;
      }
      return String(left.label || "").localeCompare(String(right.label || ""), "zh-Hans-CN");
    });
    return nodes;
  }

  function renderPapersPage() {
    if (!papersIndex || !papersMain) return;
    const sources = sourceNodesSorted();
    papersIndex.innerHTML = "";
    sources.forEach((node) => {
      const button = document.createElement("button");
      button.className = "paper-item";
      button.type = "button";
      button.setAttribute("aria-current", state.ui.selectedNodeId === node.id ? "true" : "false");
      button.innerHTML = `
        <div class="paper-item__meta"><span>${escapeHtml(node.publish_date || "未知日期")}</span><span>${escapeHtml(atlasConfidenceLabel(node.confidence))}</span></div>
        <div class="paper-item__title">${escapeHtml(node.label)}</div>
        <div class="paper-item__summary">${escapeHtml(node.summary || "暂无摘要。")}</div>
        <div class="paper-item__footer"><span>${escapeHtml(node.community || "未归入主题路线")}</span><span class="paper-item__badge">材料</span></div>
      `;
      button.addEventListener("click", () => {
        state.ui.selectedNodeId = node.id;
        renderPapersPage();
        renderReaderPreview(node);
      });
      papersIndex.appendChild(button);
    });
    if (!sources.length) {
      const empty = document.createElement("div");
      empty.className = "note-card";
      empty.textContent = "暂无材料节点。";
      papersIndex.appendChild(empty);
    }
    const selected = getSelectedNode();
    if (selected && selected.type === "source") {
      renderReaderPreview(selected);
    }
  }

  function renderReaderPreview(node) {
    if (!papersMain) return;
    if (!node) {
      papersMain.innerHTML = `<div class="reader-empty"><div><strong>从左侧选择一条材料</strong><span>这里会显示材料摘要、图和打开当前 wiki 页面入口。</span></div></div>`;
      return;
    }
    const heroImage = Array.isArray(node.images) && node.images.length ? node.images[0] : "";
    const excerpt = stripAtlasMarkdown(node.content || "").slice(0, 360);
    papersMain.innerHTML = `
      <section class="paper-spotlight">
        <div class="paper-spotlight__meta">
          <span class="paper-spotlight__pill">${escapeHtml(node.publish_date || "未知日期")}</span>
          <span class="paper-spotlight__pill">${escapeHtml(atlasTypeLabel(node.type))}</span>
          <span class="paper-spotlight__pill">${escapeHtml(atlasConfidenceLabel(node.confidence))}</span>
        </div>
        <h2>${escapeHtml(node.label)}</h2>
        <div class="paper-spotlight__actions">
          <button class="primary-button" type="button" id="open-reader">打开页面</button>
          <button class="ghost-button" type="button" id="focus-on-graph">在图谱中定位</button>
        </div>
        <div class="paper-spotlight__body">
          <div>
            <div class="summary-card">${escapeHtml(node.summary || "暂无摘要。")}</div>
            <p>${escapeHtml(excerpt || "暂无正文摘录。")}</p>
          </div>
          <div>${heroImage ? `<img src="${escapeHtml(heroImage)}" alt="${escapeHtml(node.label)}">` : `<div class="note-card">这条材料当前没有图像预览。</div>`}</div>
        </div>
      </section>
    `;
    const openReader = document.getElementById("open-reader");
    if (openReader) openReader.addEventListener("click", () => openWikiPage(node));
    const focusOnGraph = document.getElementById("focus-on-graph");
    if (focusOnGraph) {
      focusOnGraph.addEventListener("click", () => {
        state.ui.route = "graph";
        renderModeTabs();
        focusNode(node.id, true);
      });
    }
  }

  function nodeWikiUrl(node) {
    if (!node) return "";
    if (node.url) return node.url;
    const raw = node.slug || node.label || node.id || "";
    const slug = String(raw)
      .trim()
      .toLowerCase()
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/[^a-z0-9\u4e00-\u9fff]+/g, "-")
      .replace(/^-+|-+$/g, "");
    const id = encodeURIComponent(slug || String(node.id || ""));
    if (node.type === "source") return `/wiki/source/${id}`;
    if (node.type === "topic") return `/wiki/topic/${id}`;
    if (node.type === "synthesis") return `/wiki/synthesis/${id}`;
    return "/wiki";
  }

  function openWikiPage(node) {
    const href = nodeWikiUrl(node);
    if (!href) return;
    const targetWindow = window.top && window.top !== window ? window.top : window;
    targetWindow.location.href = href;
  }

  function openReaderForNode(node) {
    openWikiPage(node);
  }

  function renderModeTabs() {
    document.querySelectorAll(".mode-tab[data-route]").forEach((button) => {
      button.setAttribute("aria-pressed", button.dataset.route === (state.ui.route || "graph") ? "true" : "false");
    });
  }

  function renderCanvas() {
    const visible = state.visible || refreshVisibleSnapshot();
    atlas.dataset.mode = state.ui.dataMode;
    atlas.dataset.density = visible.densityMode;

    edgeLayer.innerHTML = "";
    visible.edges.forEach((edge) => {
      const source = state.atlasModel.byId[edge.source];
      const target = state.atlasModel.byId[edge.target];
      if (!source || !target) return;
      const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
      path.setAttribute("d", makePath(source, target, edge));
      path.setAttribute("class", `edge ${edgeClass(edge)}`);
      path.setAttribute("data-from", edge.source);
      path.setAttribute("data-to", edge.target);
      path.setAttribute("data-edge-id", edge.id);
      path.style.strokeWidth = edgeStrokeWidth(edge);
      path.style.opacity = edgeOpacity(edge);
      edgeLayer.appendChild(path);
    });

    nodeLayer.innerHTML = "";
    const previewNodeId = null;
    visible.nodes.forEach((node) => {
      const displayMode = nodeDisplayMode(node, previewNodeId);
      const visualRole = nodeVisualRole(node, displayMode, previewNodeId);
      const button = document.createElement("button");
      button.className = "node";
      if (node.unavailable) button.classList.add("is-disabled");
      if (displayMode === "compact-card") button.classList.add("is-compact");
      if (displayMode === "point") button.classList.add("is-point");
      if (displayMode === "overview") button.classList.add("is-overview");
      if (visualRole === "index-slip") button.classList.add("is-index-slip");
      if (visualRole === "cinnabar-note") button.classList.add("is-cinnabar-note");
      if (visualRole === "map-pin") button.classList.add("is-map-pin");
      if (state.visible && !state.visible.labelNodeIds[node.id]) button.classList.add("is-label-hidden");
      button.type = "button";
      button.dataset.id = node.id;
      button.dataset.type = node.type;
      button.dataset.community = node.community;
      button.dataset.densityMode = displayMode;
      button.dataset.visualRole = visualRole;
      button.dataset.startNode = "false";
      button.dataset.previewStart = "false";
      button.style.left = `${node.x}%`;
      button.style.top = `${node.y}%`;
      button.title = node.label;
      button.setAttribute("aria-pressed", node.id === state.ui.selectedNodeId ? "true" : "false");
      button.innerHTML = `
        <span class="node-kind">${node.kind}</span>
        <span class="node-name">${escapeHtml(node.label)}</span>
        <span class="node-meta"><i class="spark"></i>${escapeHtml(nodeMetaLabel(node))}</span>
      `;
      button.addEventListener("click", () => selectNode(node.id));
      button.addEventListener("mouseenter", () => highlightNeighborhood(node.id));
      button.addEventListener("mouseleave", () => applyFilters());
      nodeLayer.appendChild(button);
    });

    applyFilters();
    renderMinimap();
    applyViewportTransform();
  }

  function setDrawerActions(mode, node) {
    const queueAction = document.getElementById("queue-action");
    const sourceAction = document.getElementById("source-action");
    if (queueAction) {
      queueAction.textContent = "打开页面";
      queueAction.disabled = !node;
    }
    if (sourceAction) {
      sourceAction.textContent = "打开页面";
      sourceAction.disabled = !node;
    }
  }

  function renderStartPreview(entry) {
    const node = entry && entry.node;
    if (!node) return false;
    const neighbors = getNeighbors(node.id);
    const community = state.atlasModel.communityById[node.community];
    const communityLabel = community ? community.label : "未归入主题路线";
    const excerpt = stripAtlasMarkdown(node.content || node.summary || "").slice(0, 220);

    document.getElementById("drawer-kind").innerHTML = `<span class="spark"></span>从这里开始 · 预览`;
    document.getElementById("drawer-title").textContent = node.label;
    document.getElementById("drawer-subtitle").textContent = `${entry.reason || atlasTypeLabel(node.type)} · ${communityLabel} · 点击后在图谱中定位`;
    document.getElementById("drawer-summary").textContent = node.summary || excerpt || "这个节点适合作为当前图谱的起点。";
    document.getElementById("drawer-neighbor-count").textContent = `${neighbors.length} 个`;

    const content = document.getElementById("drawer-content");
    if (content) {
      content.innerHTML = `
        <p>这是一条节点预览。点击左侧列表或图谱节点后，可以定位并打开对应页面。</p>
        <p>${escapeHtml(excerpt || node.summary || "当前节点暂无正文，但可以从相邻节点继续展开。")}</p>
      `;
    }

    if (neighborList) {
      neighborList.innerHTML = "";
      if (!neighbors.length) {
        const empty = document.createElement("div");
        empty.className = "note-card";
        empty.textContent = "这个起点暂时没有相邻节点。";
        neighborList.appendChild(empty);
      }
      neighbors.slice(0, 4).forEach((entryItem) => {
        const neighbor = entryItem.node;
        const button = document.createElement("button");
        button.className = "neighbor-card";
        button.type = "button";
        button.innerHTML = `<span class="card-copy"><strong>${escapeHtml(neighbor.label)}</strong><span>${atlasTypeLabel(neighbor.type)} · ${atlasConfidenceLabel(entryItem.edge.type)}</span></span>`;
        button.addEventListener("click", () => focusNode(neighbor.id, true));
        neighborList.appendChild(button);
      });
    }

    setDrawerActions("preview", node);
    return true;
  }

  function renderDrawer() {
    const selected = getSelectedNode();
    if (!drawer) return;
    if (app) {
      app.dataset.reading = selected ? "1" : "0";
      app.dataset.startPreview = "0";
    }
    drawer.dataset.state = selected ? "reading" : "empty";
    if (!selected) {
      setDrawerActions("empty", null);
      document.getElementById("drawer-kind").innerHTML = `<span class="spark"></span>图谱导航`;
      document.getElementById("drawer-title").textContent = "选择一个节点";
      document.getElementById("drawer-subtitle").textContent = "综述、主题和材料共用同一份 Wiki 数据";
      document.getElementById("drawer-summary").textContent = "从左侧列表或中间图谱选择节点后，这里显示摘要、关联节点和对应页面入口。";
      document.getElementById("drawer-neighbor-count").textContent = "0 个";
      const content = document.getElementById("drawer-content");
      if (content) content.innerHTML = "<p>图谱只负责导航关系，完整内容进入对应的综述、主题或材料页面阅读。</p>";
      if (neighborList) {
        neighborList.innerHTML = "";
        const empty = document.createElement("div");
        empty.className = "note-card";
        empty.textContent = "暂无相邻节点。";
        neighborList.appendChild(empty);
      }
      return;
    }
    state.ui.selectedNodeId = selected.id;
    setDrawerActions("reading", selected);

    const neighbors = getNeighbors(selected.id);
    document.getElementById("drawer-kind").innerHTML = `<span class="spark"></span>${atlasTypeLabel(selected.type)} · 已选中`;
    document.getElementById("drawer-title").textContent = selected.label;
    document.getElementById("drawer-subtitle").textContent = `${atlasTypeLabel(selected.type)} · ${atlasConfidenceLabel(selected.confidence)}${selected.source_path ? " · " + selected.source_path : ""}`;
    document.getElementById("drawer-summary").textContent = selected.summary || "暂无摘要。";
    document.getElementById("drawer-neighbor-count").textContent = `${neighbors.length} 个`;

    renderKnowledgeCard(selected, neighbors);

    if (neighborList) {
      neighborList.innerHTML = "";
      if (!neighbors.length) {
        const empty = document.createElement("div");
        empty.className = "note-card";
        empty.textContent = "这个节点暂时没有相邻节点。";
        neighborList.appendChild(empty);
      }
      neighbors.forEach((entry) => {
        const node = entry.node;
        const button = document.createElement("button");
        button.className = "neighbor-card";
        button.type = "button";
        button.innerHTML = `<span class="card-copy"><strong>${escapeHtml(node.label)}</strong><span>${atlasTypeLabel(node.type)} · ${atlasConfidenceLabel(entry.edge.type)}</span></span>`;
        button.addEventListener("click", () => focusNode(node.id, true));
        neighborList.appendChild(button);
      });
    }
  }

  function renderKnowledgeCard(node, neighbors) {
    const content = document.getElementById("drawer-content");
    if (!content) return;
    const excerpt = stripAtlasMarkdown(node.content || node.summary || "").slice(0, 220);
    const related = neighbors.length
      ? `当前连接到 ${neighbors.slice(0, 4).map((entry) => `「${entry.node.label}」`).join("、")}。`
      : "这个节点暂时没有相邻节点。";
    content.innerHTML = `
      <p>${escapeHtml(node.label)} 是知识库中的「${escapeHtml(atlasTypeLabel(node.type))}」节点。完整内容由当前 wiki 页面维护，图谱这里只保留摘要和关系。</p>
      <p>${escapeHtml(excerpt || node.summary || related)}</p>
    `;
  }

  function getNeighbors(nodeId) {
    const out = [];
    state.atlasModel.edges.forEach((edge) => {
      if (edge.source === nodeId && state.atlasModel.byId[edge.target]) {
        out.push({ node: state.atlasModel.byId[edge.target], edge, direction: "to" });
      } else if (edge.target === nodeId && state.atlasModel.byId[edge.source]) {
        out.push({ node: state.atlasModel.byId[edge.source], edge, direction: "from" });
      }
    });
    return out.sort((left, right) => clampWeight(right.edge.weight) - clampWeight(left.edge.weight));
  }

  function renderInsights() {
    if (!insightTitle || !insightCopy) return;
    const visible = state.visible || refreshVisibleSnapshot();
    const insights = state.atlasModel.insights;
    const bridge = insights.bridge_nodes && insights.bridge_nodes[0];
    const surprising = insights.surprising_connections && insights.surprising_connections[0];
    if (surprising) {
      insightTitle.textContent = "发现跨层级连接";
      insightCopy.textContent = `${surprising.from} 与 ${surprising.to} 的关系权重较高，适合作为下一步阅读线索。`;
    } else if (bridge) {
      insightTitle.textContent = "桥接节点值得优先阅读";
      insightCopy.textContent = `${bridge.label || bridge.id} 连接多个节点，可帮助从局部材料进入全局图谱。`;
    } else if (visible.densityMode === "overview") {
      insightTitle.textContent = "当前视图过密";
      insightCopy.textContent = "建议搜索关键词，或只看综述、主题、材料中的一类。";
    } else {
      insightTitle.textContent = "从选中节点打开页面";
      insightCopy.textContent = "右侧详情会随节点和筛选同步更新，完整内容进入对应 Wiki 页面阅读。";
    }
  }

  function renderMinimap() {
    if (!minimapSvg) return;
    const visible = state.visible || refreshVisibleSnapshot();
    while (minimapSvg.firstChild) minimapSvg.removeChild(minimapSvg.firstChild);
    const ns = "http://www.w3.org/2000/svg";
    const path = document.createElementNS(ns, "path");
    path.setAttribute("d", "M8 40 C34 20 54 36 76 22 C98 8 118 24 150 12");
    path.setAttribute("fill", "none");
    path.setAttribute("stroke", "#cfc4b1");
    path.setAttribute("stroke-width", "1.4");
    minimapSvg.appendChild(path);

    visible.nodes.slice(0, 60).forEach((node) => {
      const point = atlasPointToMinimap(atlasNodePoint(node));
      const circle = document.createElementNS(ns, "circle");
      circle.setAttribute("cx", String(point.x));
      circle.setAttribute("cy", String(point.y));
      circle.setAttribute("r", node.id === state.ui.selectedNodeId ? "3.2" : "2.2");
      circle.setAttribute("fill", communityColor(node.community));
      if (node.id === state.ui.selectedNodeId) circle.classList.add("is-selected");
      minimapSvg.appendChild(circle);
    });

    const rect = document.createElementNS(ns, "rect");
    rect.setAttribute("class", "mini-map-viewport");
    rect.setAttribute("rx", "5");
    minimapSvg.appendChild(rect);
    updateMinimapViewport();
  }

  function applyFilters() {
    const visible = state.visible || refreshVisibleSnapshot();
    const visibleIds = new Set(visible.node_ids);
    const selectedIds = state.ui.selectedNodeId ? connectedIds(state.ui.selectedNodeId) : new Set();

    document.querySelectorAll(".node").forEach((nodeEl) => {
      const id = nodeEl.dataset.id;
      const isVisible = visibleIds.has(id);
      nodeEl.classList.toggle("is-hidden", !isVisible);
      const dim = state.ui.dimUnselected && state.ui.selectedNodeId && !selectedIds.has(id);
      nodeEl.classList.toggle("is-dim", isVisible && dim);
      nodeEl.setAttribute("aria-pressed", id === state.ui.selectedNodeId ? "true" : "false");
    });

    document.querySelectorAll(".edge").forEach((edgeEl) => {
      const from = edgeEl.dataset.from;
      const to = edgeEl.dataset.to;
      const visibleEdge = visibleIds.has(from) && visibleIds.has(to);
      const dim = state.ui.dimUnselected && state.ui.selectedNodeId && from !== state.ui.selectedNodeId && to !== state.ui.selectedNodeId;
      edgeEl.classList.toggle("is-dim", !visibleEdge || dim);
    });

    const hasNoResults = !!state.ui.query && visible.nodes.length === 0 && state.ui.dataMode === "normal";
    if (noResults) noResults.classList.toggle("is-visible", hasNoResults);

    const focusLabel = ({
      all: "全部",
      synthesis: "综述判断",
      topic: "主题路线",
      source: "材料"
    })[state.ui.focusMode] || "全部";
    const scopedNode = state.ui.scopedNodeId ? state.atlasModel.byId[state.ui.scopedNodeId] : null;
    if (canvasTitle) canvasTitle.textContent = scopedNode ? `知识图谱 · ${scopedNode.label}` : `知识图谱 · ${focusLabel}`;
    if (canvasSubtitle) {
      const densityLabel = ({
        card: "卡片",
        "compact-card": "紧凑卡片",
        "point-plus-focus": "点位聚焦",
        overview: "总览"
      })[visible.densityMode] || "卡片";
      canvasSubtitle.textContent = hasNoResults
        ? "当前筛选没有匹配节点"
        : scopedNode
          ? `${visible.nodes.length} 个关联节点可见 · ${densityLabel}模式`
          : `${visible.nodes.length} 个节点可见 · ${densityLabel}模式`;
    }
  }

  function highlightNeighborhood(id) {
    if (state.ui.dataMode !== "normal") return;
    const ids = connectedIds(id);
    document.querySelectorAll(".node").forEach((nodeEl) => {
      nodeEl.classList.toggle("is-dim", !ids.has(nodeEl.dataset.id));
    });
    document.querySelectorAll(".edge").forEach((edgeEl) => {
      edgeEl.classList.toggle("is-dim", edgeEl.dataset.from !== id && edgeEl.dataset.to !== id);
    });
  }

  function renderAtlasView(options) {
    const opts = options && typeof options === "object" ? options : {};
    refreshVisibleSnapshot();
    if (app) app.dataset.reading = state.ui.selectedNodeId ? "1" : "0";
    if (app) app.dataset.route = state.ui.route || "graph";
    if (opts.fitViewport || !state.viewportReady) fitVisibleViewport();
    renderTopbar();
    renderSidebar();
    renderCanvas();
    renderDrawer();
    renderInsights();
    renderPapersPage();
  }

  function selectNode(id) {
    const node = state.atlasModel.byId[id];
    if (!node) return;
    if (node.type === "topic" || node.type === "synthesis") state.ui.scopedNodeId = node.id;
    state.ui.selectedNodeId = id;
    renderAtlasView();
  }

  function focusNode(nodeId, openDrawer) {
    const node = state.atlasModel.byId[nodeId];
    if (!node) return;
    if (node.type === "topic" || node.type === "synthesis") state.ui.scopedNodeId = node.id;
    state.ui.selectedNodeId = nodeId;
    if (openDrawer !== false && drawer) {
      drawer.scrollIntoView({ block: "nearest", inline: "nearest" });
    }
    renderAtlasView();
    centerViewportOnNode(nodeId);
  }

  function closeDrawer() {
    state.ui.selectedNodeId = null;
    state.ui.scopedNodeId = null;
    renderAtlasView({ fitViewport: true });
  }

  function setCommunity(communityId) {
    state.ui.activeCommunityId = communityId || "all";
    renderAtlasView({ fitViewport: true });
  }

  function buildNoteText(node) {
    const stripped = stripAtlasMarkdown(node && node.content);
    const excerpt = stripped.slice(0, NOTE_EXCERPT_LIMIT);
    return node && node.label ? `${node.label}${excerpt ? "：" + excerpt : ""}` : excerpt;
  }

  function handleQueueAction() {
    const node = getSelectedNode();
    if (!node) {
      const previewEntry = getPreviewStartEntry();
      if (previewEntry && previewEntry.node) focusNode(previewEntry.node.id, true);
      return;
    }
    state.queue = toggleQueueFavorite(state.queue, node.id);
    state.queue = appendQueueNote(state.queue, {
      id: `${node.id}:${Date.now()}`,
      node_id: node.id,
      label: node.label,
      text: buildNoteText(node),
      created_at: new Date().toISOString()
    }, QUEUE_NOTE_LIMIT);
    persistQueueState();
    renderSidebar();
  }

  function setupSearch() {
    if (!searchInput) return;
    searchInput.addEventListener("input", () => {
      state.ui.query = searchInput.value.trim().toLowerCase();
      renderAtlasView({ fitViewport: true });
    });
    searchInput.addEventListener("keydown", (event) => {
      if (event.key !== "Enter") return;
      const hit = state.visible && state.visible.nodes[0];
      if (hit) focusNode(hit.id, true);
    });
  }

  function isCanvasPanTarget(target) {
    return !(target && target.closest && target.closest(".node, button, a, input, textarea, summary, details"));
  }

  function setupViewportInteractions() {
    atlas.addEventListener("pointerdown", (event) => {
      if (event.button !== 0 || !isCanvasPanTarget(event.target)) return;
      panState = {
        pointerId: event.pointerId,
        startX: event.clientX,
        startY: event.clientY,
        viewport: { x: state.viewport.x, y: state.viewport.y, scale: state.viewport.scale }
      };
      atlas.classList.add("is-panning");
      atlas.setPointerCapture(event.pointerId);
      event.preventDefault();
    });

    atlas.addEventListener("pointermove", (event) => {
      if (!panState || panState.pointerId !== event.pointerId) return;
      setViewport({
        x: panState.viewport.x + event.clientX - panState.startX,
        y: panState.viewport.y + event.clientY - panState.startY,
        scale: panState.viewport.scale
      });
      event.preventDefault();
    });

    function finishPan(event) {
      if (!panState || panState.pointerId !== event.pointerId) return;
      panState = null;
      atlas.classList.remove("is-panning");
      if (atlas.hasPointerCapture && atlas.hasPointerCapture(event.pointerId)) {
        atlas.releasePointerCapture(event.pointerId);
      }
    }

    atlas.addEventListener("pointerup", finishPan);
    atlas.addEventListener("pointercancel", finishPan);
    atlas.addEventListener("wheel", (event) => {
      if (!isCanvasPanTarget(event.target) && !(event.target && event.target.closest && event.target.closest(".node"))) return;
      const rect = atlas.getBoundingClientRect();
      const factor = Math.exp(-event.deltaY * 0.0012);
      setViewport(zoomAtlasViewport(state.viewport, factor, {
        x: event.clientX - rect.left,
        y: event.clientY - rect.top
      }, currentViewportSize(), viewportOptions()));
      event.preventDefault();
    }, { passive: false });
  }

  function setupMinimapNavigation() {
    if (!minimapSvg) return;
    minimapSvg.addEventListener("click", (event) => {
      const matrix = minimapSvg.getScreenCTM && minimapSvg.getScreenCTM();
      if (!matrix) return;
      const point = minimapSvg.createSVGPoint();
      point.x = event.clientX;
      point.y = event.clientY;
      const local = point.matrixTransform(matrix.inverse());
      const atlasPoint = minimapPointToAtlasPoint({ x: local.x, y: local.y });
      setViewport(centerAtlasViewportOnPoint(atlasPoint, currentViewportSize(), state.viewport.scale, viewportOptions()), true);
    });
  }

  function setupControls() {
    document.querySelectorAll(".mode-tab[data-route]").forEach((button) => {
      button.addEventListener("click", () => {
        state.ui.route = button.dataset.route || "graph";
        renderModeTabs();
        if (app) app.dataset.route = state.ui.route;
        if (state.ui.route === "papers") {
          renderPapersPage();
        } else if (state.ui.route === "reader") {
          const node = getSelectedNode();
          if (node && node.type === "source") openReaderForNode(node);
          else state.ui.route = "graph";
        } else {
          renderAtlasView();
        }
      });
    });

    document.querySelectorAll("[data-focus]").forEach((button) => {
      button.addEventListener("click", () => {
        state.ui.focusMode = button.dataset.focus || "all";
        state.ui.scopedNodeId = null;
        state.ui.selectedNodeId = null;
        document.querySelectorAll("[data-focus]").forEach((item) => {
          item.setAttribute("aria-pressed", item === button ? "true" : "false");
        });
        renderAtlasView({ fitViewport: true });
      });
    });

    const queueAction = document.getElementById("queue-action");
    if (queueAction) {
      queueAction.addEventListener("click", () => {
        const node = getSelectedNode();
        if (node) openWikiPage(node);
      });
    }

    const sourceAction = document.getElementById("source-action");
    if (sourceAction) {
      sourceAction.addEventListener("click", () => {
        const node = getSelectedNode();
        if (node) openWikiPage(node);
      });
    }

    const readerBackGraph = document.getElementById("reader-back-graph");
    if (readerBackGraph) {
      readerBackGraph.addEventListener("click", () => {
        state.ui.route = "graph";
        renderModeTabs();
        renderAtlasView();
      });
    }

    const readerBackPapers = document.getElementById("reader-back-papers");
    if (readerBackPapers) {
      readerBackPapers.addEventListener("click", () => {
        state.ui.route = "papers";
        renderModeTabs();
        if (app) app.dataset.route = "papers";
        renderPapersPage();
      });
    }

    if (papersSearch) {
      papersSearch.addEventListener("input", () => {
        state.ui.papersQuery = papersSearch.value.trim();
        renderPapersPage();
      });
    }
    if (papersSort) {
      papersSort.addEventListener("change", () => {
        state.ui.papersSort = papersSort.value || "date-desc";
        renderPapersPage();
      });
    }
  }

  function applyNeighborsCollapsed(collapsed) {
    if (!drawerNeighbors || !drawerNeighborsHeading) return;
    drawerNeighbors.open = !collapsed;
    drawerNeighbors.setAttribute("data-collapsed", collapsed ? "1" : "0");
    drawerNeighborsHeading.setAttribute("aria-expanded", collapsed ? "false" : "true");
  }

  function toggleNeighbors() {
    if (!drawerNeighbors) return;
    const nextCollapsed = drawerNeighbors.open;
    applyNeighborsCollapsed(nextCollapsed);
    safeLocalStorage.set(queueStorageKey("neighbors-collapsed"), nextCollapsed ? "1" : "0");
  }

  function setupNeighborToggle() {
    if (!drawerNeighbors || !drawerNeighborsHeading) return;
    applyNeighborsCollapsed(false);
    drawerNeighbors.addEventListener("toggle", () => {
      if (!drawerNeighbors.open) {
        applyNeighborsCollapsed(false);
        return;
      }
      state.ui.neighborExpanded = drawerNeighbors.open;
      drawerNeighbors.setAttribute("data-collapsed", "0");
      drawerNeighborsHeading.setAttribute("aria-expanded", "true");
    });
    drawerNeighborsHeading.addEventListener("click", (e) => {
      e.preventDefault();
      applyNeighborsCollapsed(false);
    });
    drawerNeighborsHeading.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        applyNeighborsCollapsed(false);
      }
    });
  }

  function applyMinimapCollapsed(collapsed) {
    if (!minimapEl || !minimapToggle) return;
    minimapEl.setAttribute("data-collapsed", collapsed ? "1" : "0");
    minimapToggle.setAttribute("aria-expanded", collapsed ? "false" : "true");
    minimapToggle.setAttribute("aria-label", collapsed ? "展开小地图" : "折叠小地图");
  }

  setupSearch();
  setupViewportInteractions();
  setupMinimapNavigation();
  setupControls();
  setupNeighborToggle();
  applyMinimapCollapsed(false);
  window.addEventListener("resize", () => renderAtlasView({ fitViewport: true }));
  renderAtlasView({ fitViewport: true });
  renderModeTabs();
})();
