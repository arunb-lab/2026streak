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

from datetime import date
from typing import Any

from fastapi import FastAPI, Query, Response
from pydantic import BaseModel, Field

from project.date_range import DateRange
from project.heatmap import build_heatmap
from project.heatmap_svg import render_svg

app = FastAPI(title="2026streak Mini API", version="0.2.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


def _parse_holidays_csv(raw: str | None) -> set[date]:
    if raw is None or not raw.strip():
        return set()
    out: set[date] = set()
    for part in raw.split(","):
        p = part.strip()
        if not p:
            continue
        out.add(date.fromisoformat(p))
    return out


@app.get("/daterange/info")
def daterange_info(
    range: str = Query(..., description="YYYY-MM-DD..YYYY-MM-DD"),
    business_days: bool = Query(False, description="Count only Mon–Fri"),
    shift_days: int = Query(0, description="Shift the range by N days"),
    holidays: str | None = Query(
        None,
        description=(
            "Comma-separated YYYY-MM-DD dates to exclude from business day count"
        ),
        examples=["2026-01-01,2026-01-02"],
    ),
) -> dict[str, Any]:
    r = DateRange.from_iso(range).shift(days=shift_days)
    holiday_set = _parse_holidays_csv(holidays)

    bd = r.business_days()
    bd_ex = r.business_days(holidays=holiday_set)
    count = bd_ex if business_days else r.days()

    return {
        "range": r.to_iso(),
        "start": r.start.isoformat(),
        "end": r.end.isoformat(),
        "days": r.days(),
        "business_days": bd,
        "holidays": sorted(d.isoformat() for d in holiday_set),
        "business_days_excluding_holidays": bd_ex,
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


class HeatmapRequest(BaseModel):
    start: date = Field(..., description="Start date (YYYY-MM-DD)")
    end: date = Field(..., description="End date (YYYY-MM-DD)")
    counts: dict[date, int] = Field(
        default_factory=dict,
        description="Mapping of date -> count",
        examples=[{"2026-01-01": 3, "2026-01-02": 0, "2026-01-03": 7}],
    )


@app.post("/heatmap/data")
def heatmap_data(req: HeatmapRequest) -> dict[str, Any]:
    h = build_heatmap(req.start, req.end, req.counts)
    # Flattened list is easier to consume in clients.
    cells = [
        {"date": c.day.isoformat(), "count": c.count}
        for col in h.weeks
        for c in col
        if c is not None
    ]
    return {
        "start": req.start.isoformat(),
        "end": req.end.isoformat(),
        "weeks": h.width,
        "cells": cells,
    }


@app.post("/heatmap/svg")
def heatmap_svg(req: HeatmapRequest) -> Response:
    h = build_heatmap(req.start, req.end, req.counts)
    svg = render_svg(h, title=f"{req.start.isoformat()}..{req.end.isoformat()}")
    return Response(content=svg, media_type="image/svg+xml")
