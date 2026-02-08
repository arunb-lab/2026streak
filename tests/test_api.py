from __future__ import annotations

from datetime import date

from fastapi.testclient import TestClient

from project.api import app


def test_health() -> None:
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_daterange_info_days() -> None:
    client = TestClient(app)
    r = client.get("/daterange/info", params={"range": "2026-01-01..2026-01-04"})
    assert r.status_code == 200
    data = r.json()
    assert data["range"] == "2026-01-01..2026-01-04"
    assert data["days"] == 4
    assert data["business_days"] == 2
    assert data["business_days_excluding_holidays"] == 2
    assert data["count"] == 4


def test_daterange_info_business_days_and_shift() -> None:
    client = TestClient(app)
    r = client.get(
        "/daterange/info",
        params={
            "range": "2026-01-01..2026-01-04",
            "business_days": True,
            "shift_days": 1,
        },
    )
    assert r.status_code == 200
    data = r.json()
    assert data["range"] == "2026-01-02..2026-01-05"
    assert data["count"] == 2


def test_daterange_info_business_days_with_holidays() -> None:
    client = TestClient(app)
    r = client.get(
        "/daterange/info",
        params={
            "range": "2026-01-01..2026-01-04",
            "business_days": True,
            "holidays": "2026-01-02",
        },
    )
    assert r.status_code == 200
    data = r.json()
    assert data["business_days"] == 2
    assert data["business_days_excluding_holidays"] == 1
    assert data["count"] == 1


def test_daterange_split() -> None:
    client = TestClient(app)
    r = client.get(
        "/daterange/split",
        params={"range": "2026-01-01..2026-01-05", "chunk_days": 2},
    )
    assert r.status_code == 200
    assert r.json()["chunks"] == [
        "2026-01-01..2026-01-02",
        "2026-01-03..2026-01-04",
        "2026-01-05..2026-01-05",
    ]


def test_heatmap_svg_endpoint() -> None:
    client = TestClient(app)
    payload = {
        "start": date(2026, 1, 1).isoformat(),
        "end": date(2026, 1, 3).isoformat(),
        "counts": {"2026-01-01": 1, "2026-01-02": 2, "2026-01-03": 3},
    }
    r = client.post("/heatmap/svg", json=payload)
    assert r.status_code == 200
    assert r.headers["content-type"].startswith("image/svg+xml")
    assert r.text.count("<rect") == 3
