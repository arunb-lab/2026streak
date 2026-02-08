"""Small project modules.

This folder contains slightly more "resume-ready" code than the scratch scripts
elsewhere in the repo.

Highlights:
- :mod:`project.date_range` – date interval utilities
- :mod:`project.heatmap` + :mod:`project.heatmap_svg` – GitHub-style heatmap SVG
"""

from project.date_range import DateRange, merge_overlapping
from project.heatmap import Heatmap, HeatmapCell, build_heatmap
from project.heatmap_svg import SvgOptions, render_svg

__all__ = [
    "DateRange",
    "merge_overlapping",
    "Heatmap",
    "HeatmapCell",
    "build_heatmap",
    "SvgOptions",
    "render_svg",
]
