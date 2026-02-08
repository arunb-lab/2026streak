from __future__ import annotations

from datetime import date

import pytest

from project.heatmap import build_heatmap
from project.heatmap_svg import SvgOptions, render_svg


def test_render_svg_rejects_short_palette() -> None:
    h = build_heatmap(date(2026, 1, 1), date(2026, 1, 1), {date(2026, 1, 1): 1})
    with pytest.raises(ValueError):
        render_svg(h, opts=SvgOptions(palette=["#000"]))
