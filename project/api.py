"""FastAPI mini-service.

This is a small, practical API layer on top of the DateRange utilities.
It exists mainly as a "hireable" signal: typed core logic + a thin web API + tests.

Run locally (from repo root):
    python -m pip install fastapi uvicorn
    uvicorn project.api:app --reload

Then open:
    http://127.0.0.1:8000/docs
"""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI, Query

from project.date_range import DateRange

app = FastAPI(title="2026streak DateRange API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/daterange/info")
def daterange_info(
    range: str = Query(..., description="YYYY-MM-DD..YYYY-MM-DD"),
    business_days: bool = Query(False, description="Count only Mon–Fri"),
    shift_days: int = Query(0, description="Shift the range by N days"),
) -> dict[str, Any]:
    r = DateRange.from_iso(range).shift(days=shift_days)
    count = r.business_days() if business_days else r.days()
    return {
        "range": r.to_iso(),
        "start": r.start.isoformat(),
        "end": r.end.isoformat(),
        "days": r.days(),
        "business_days": r.business_days(),
        "count": count,
    }


@app.get("/daterange/split")
def daterange_split(
    range: str = Query(..., description="YYYY-MM-DD..YYYY-MM-DD"),
    chunk_days: int = Query(..., gt=0, description="Chunk size in days (> 0)"),
) -> dict[str, Any]:
    r = DateRange.from_iso(range)
    chunks = r.split(chunk_days=chunk_days)
    return {
        "range": r.to_iso(),
        "chunk_days": chunk_days,
        "chunks": [c.to_iso() for c in chunks],
    }
