# Architecture notes

This service is intentionally small, but structured to scale.

## Decisions

- **App factory** (`create_app()`): keeps global state explicit and tests fast.
- **In-memory store**: avoids DB setup while still demonstrating a clean boundary.
- **Typed models**: request/response models are Pydantic-based.
- **Error shape**: `ErrorResponse` gives a consistent JSON contract for simple errors.

## If you want to productionize

- Replace `TodoStore` with a repository backed by Postgres/SQLite.
- Add structured logging + request IDs.
- Add auth (API key / OAuth) and rate limiting.
- Add OpenTelemetry tracing.
