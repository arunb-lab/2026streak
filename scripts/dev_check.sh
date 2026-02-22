#!/usr/bin/env bash
set -euo pipefail

python -m pip install -U pip
python -m pip install -r requirements-dev.txt

ruff check .
pytest
