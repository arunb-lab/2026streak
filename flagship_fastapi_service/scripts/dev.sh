#!/usr/bin/env bash
set -euo pipefail

# Run the service locally with auto-reload.
# Usage: ./flagship_fastapi_service/scripts/dev.sh

exec uvicorn flagship_fastapi_service.flagship_api.app:create_app --factory --reload
