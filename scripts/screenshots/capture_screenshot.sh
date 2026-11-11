#!/usr/bin/env bash
# Capture the screenshots of the blog inside a Docker container (never on the
# host desktop, see framework/process/gui-testing.md). The repository is mounted
# read-only, the PNG files are written to docs/images.
# Usage: bash scripts/screenshots/capture_screenshot.sh --all
#        bash scripts/screenshots/capture_screenshot.sh step-03a-admin-home [step-name ...]
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && { pwd -W 2>/dev/null || pwd; })"
export MSYS_NO_PATHCONV=1
mkdir -p "$root/docs/images"
docker build -q -t blog-screenshots \
	-f "$root/scripts/screenshots/Dockerfile.screenshots" "$root/scripts/screenshots" >/dev/null
docker run --rm \
	-v "$root:/repo:ro" \
	-v "$root/docs/images:/out" \
	-e PYTHONDONTWRITEBYTECODE=1 \
	blog-screenshots \
	bash /repo/scripts/screenshots/capture_in_container.sh "$@"
