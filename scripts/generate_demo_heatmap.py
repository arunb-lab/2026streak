"""Generate a demo heatmap SVG under assets/.

Run:
  .venv/bin/python scripts/generate_demo_heatmap.py
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
import sys

# Allow running as a script without installing the package.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from project.heatmap import build_heatmap
from project.heatmap_samples import generate_sample_counts
from project.heatmap_svg import render_svg


def main() -> int:
    start = date(2026, 1, 1)
    end = date(2026, 12, 31)

    counts = generate_sample_counts(start, end, seed=2026)
    h = build_heatmap(start, end, counts)
    svg = render_svg(h, title="2026 demo contributions")

    out = Path("assets") / "heatmap-demo.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
