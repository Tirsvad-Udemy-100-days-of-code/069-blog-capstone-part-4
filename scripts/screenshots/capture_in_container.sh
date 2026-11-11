#!/usr/bin/env bash
# Runs inside the Docker container: installs a copy of the project and takes the
# screenshots. Started by capture_screenshot.sh.
set -euo pipefail
cp -r /repo /tmp/app
cd /tmp/app
rm -rf .venv framework .git .env instance
pip install -q .
python scripts/screenshots/capture_screenshot.py "$@"
