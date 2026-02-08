from __future__ import annotations

from datetime import date

from project.heatmap_samples import generate_sample_counts


def test_generate_sample_counts_is_deterministic() -> None:
    a = generate_sample_counts(date(2026, 1, 1), date(2026, 1, 31), seed=1)
    b = generate_sample_counts(date(2026, 1, 1), date(2026, 1, 31), seed=1)
    assert a == b


def test_generate_sample_counts_has_all_days() -> None:
    out = generate_sample_counts(date(2026, 1, 1), date(2026, 1, 3), seed=0)
    assert set(out.keys()) == {date(2026, 1, 1), date(2026, 1, 2), date(2026, 1, 3)}
