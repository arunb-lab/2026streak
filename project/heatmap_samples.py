"""Deterministic sample data for the heatmap.

Portfolio repos look better with a demo you can run instantly.
This module generates *fake* contribution counts that still look realistic.
"""

from __future__ import annotations

import random
from datetime import date

from project.date_range import DateRange


def generate_sample_counts(
    start: date,
    end: date,
    *,
    seed: int = 2026,
) -> dict[date, int]:
    """Generate a deterministic date->count mapping.

    Heuristics:
    - Weekends are usually lower.
    - Occasional bursts happen.
    """

    rng = random.Random(seed)
    r = DateRange(start, end)

    out: dict[date, int] = {}
    streak = 0

    for d in r.iter_days():
        is_weekend = d.weekday() >= 5
        base = 0 if is_weekend else 1

        # chance to contribute (lower on weekends)
        p = 0.75 if not is_weekend else 0.25
        if rng.random() > p:
            out[d] = 0
            streak = 0
            continue

        streak += 1

        # count increases a bit with streak length, plus randomness
        burst = 3 if rng.random() < 0.07 else 0
        out[d] = base + min(5, streak // 4) + rng.randint(0, 3) + burst

    return out
