#!/usr/bin/env bash
set -euo pipefail

PARENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
GITIGNORE="$PARENT_DIR/.gitignore"

touch "$GITIGNORE"

if ! grep -Fq "# AI Token Saver local setup/runtime folders" "$GITIGNORE"; then
  printf "\n# AI Token Saver local setup/runtime folders\n" >> "$GITIGNORE"
fi

add_line() {
  local line="$1"
  if ! grep -Fxq "$line" "$GITIGNORE"; then
    printf "%s\n" "$line" >> "$GITIGNORE"
  fi
}

add_line "--ai-token-saver-setup/"
add_line "--ai-token-saver/"

echo "Updated parent .gitignore: $GITIGNORE"
