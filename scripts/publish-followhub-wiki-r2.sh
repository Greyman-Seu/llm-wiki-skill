#!/bin/bash
# Publish a built FollowHub Wiki package.
#
# Usage:
#   bash scripts/publish-followhub-wiki-r2.sh <package_dir> local:/absolute/path
#   bash scripts/publish-followhub-wiki-r2.sh <package_dir> rclone:<remote>:<bucket-or-path>/wiki
#
# The local target is used by tests and dry runs. The rclone target is the
# intended R2 path when rclone is configured for Cloudflare R2.

set -euo pipefail

SCRIPT_DIR="${BASH_SOURCE[0]%/*}"
[ "$SCRIPT_DIR" = "${BASH_SOURCE[0]}" ] && SCRIPT_DIR="."
SCRIPT_DIR="$(cd "$SCRIPT_DIR" && pwd)"

PACKAGE_DIR="${1:-}"
TARGET="${2:-}"

if [ -z "$PACKAGE_DIR" ] || [ -z "$TARGET" ]; then
  echo "ERROR: usage: publish-followhub-wiki-r2.sh <package_dir> <local:/path|rclone:remote:path>" >&2
  exit 1
fi

if [ ! -d "$PACKAGE_DIR" ]; then
  echo "ERROR: package dir not found: $PACKAGE_DIR" >&2
  exit 1
fi

python3 "$SCRIPT_DIR/validate-followhub-wiki-package.py" "$PACKAGE_DIR"

case "$TARGET" in
  local:*)
    DEST="${TARGET#local:}"
    if [ -z "$DEST" ] || [ "$DEST" = "/" ]; then
      echo "ERROR: refusing unsafe local target: $DEST" >&2
      exit 1
    fi
    mkdir -p "$DEST"
    cp -a "$PACKAGE_DIR"/. "$DEST"/
    echo "FollowHub wiki package copied to $DEST"
    ;;
  rclone:*)
    if ! command -v rclone >/dev/null 2>&1; then
      echo "ERROR: rclone is required for rclone targets" >&2
      exit 1
    fi
    RCLONE_TARGET="${TARGET#rclone:}"
    rclone copy "$PACKAGE_DIR" "$RCLONE_TARGET" --checksum
    echo "FollowHub wiki package published to $RCLONE_TARGET"
    ;;
  *)
    echo "ERROR: unsupported target: $TARGET" >&2
    echo "       use local:/path or rclone:remote:path" >&2
    exit 1
    ;;
esac
