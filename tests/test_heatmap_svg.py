from __future__ import annotations

from datetime import date

from project.heatmap import build_heatmap
from project.heatmap_svg import render_svg


def test_render_svg_contains_rects() -> None:
    counts = {
        date(2026, 1, 1): 1,
        date(2026, 1, 2): 2,
        date(2026, 1, 3): 3,
    }
    h = build_heatmap(date(2026, 1, 1), date(2026, 1, 3), counts)
    svg = render_svg(h, title="demo")

    assert svg.startswith("<?xml")
    assert "<svg" in svg
    assert "data-date=\"2026-01-01\"" in svg
    assert svg.count("<rect") == 3
    assert "<title>demo</title>" in svg
