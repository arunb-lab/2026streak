"""SVG renderer for :mod:`project.heatmap`.

The output is a lightweight GitHub-style grid, suitable for embedding in READMEs.
No external dependencies.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape

from project.heatmap import Heatmap, HeatmapCell, max_count


DEFAULT_PALETTE = [
    "#ebedf0",  # 0
    "#9be9a8",  # 1
    "#40c463",  # 2
    "#30a14e",  # 3
    "#216e39",  # 4+
]


@dataclass(frozen=True, slots=True)
class SvgOptions:
    cell_size: int = 12
    cell_gap: int = 3
    radius: int = 2
    palette: list[str] | None = None
    show_title: bool = True


def _level(count: int, *, maxv: int) -> int:
    if count <= 0:
        return 0
    if maxv <= 1:
        return 1

    # 1..4 levels based on quartiles of the max.
    q1 = max(1, maxv // 4)
    q2 = max(2, maxv // 2)
    q3 = max(3, (3 * maxv) // 4)

    if count <= q1:
        return 1
    if count <= q2:
        return 2
    if count <= q3:
        return 3
    return 4


def render_svg(h: Heatmap, *, opts: SvgOptions | None = None, title: str = "") -> str:
    opts = opts or SvgOptions()
    palette = opts.palette or DEFAULT_PALETTE

    if len(palette) < 5:
        raise ValueError("palette must have at least 5 colors")

    cell = opts.cell_size
    gap = opts.cell_gap
    radius = opts.radius

    width = h.width * (cell + gap) - gap
    height = h.height * (cell + gap) - gap

    mc = max_count(h)

    rects: list[str] = []
    for x, col in enumerate(h.weeks):
        for y, maybe in enumerate(col):
            if maybe is None:
                continue
            c: HeatmapCell = maybe
            lvl = _level(c.count, maxv=mc)
            fill = palette[lvl]
            rx = x * (cell + gap)
            ry = y * (cell + gap)
            tip = f"{c.day.isoformat()}: {c.count}"
            rects.append(
                "<rect"
                f" x=\"{rx}\" y=\"{ry}\" width=\"{cell}\" height=\"{cell}\""
                f" rx=\"{radius}\" ry=\"{radius}\""
                f" fill=\"{escape(fill)}\""
                f" data-date=\"{c.day.isoformat()}\" data-count=\"{c.count}\""
                ">"
                f"<title>{escape(tip)}</title>"
                "</rect>"
            )

    title_tag = ""
    if opts.show_title and title.strip():
        title_tag = f"<title>{escape(title.strip())}</title>"

    header = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        f"<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"{width}\""
        f" height=\"{height}\" viewBox=\"0 0 {width} {height}\">\n"
    )

    body = "\n".join(rects)

    return (
        header
        + (f"{title_tag}\n" if title_tag else "")
        + (body + "\n" if body else "")
        + "</svg>\n"
    )
