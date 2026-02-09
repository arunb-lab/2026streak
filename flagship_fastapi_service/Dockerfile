# Simple Dockerfile for running the Flagship FastAPI service
# (kept optional; the repo CI does not depend on Docker)

FROM python:3.12-slim

WORKDIR /app

# Install runtime deps
RUN pip install --no-cache-dir fastapi uvicorn

# Copy just the service code (not the whole repo)
COPY flagship_api ./flagship_api

EXPOSE 8000

CMD ["uvicorn", "flagship_api.app:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
