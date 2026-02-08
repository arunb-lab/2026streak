from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pytest

from project.heatmap_cli import _load_counts


def test_load_counts_parses_iso_dates(tmp_path: Path) -> None:
    p = tmp_path / "counts.json"
    p.write_text(json.dumps({"2026-01-01": 2, "2026-01-02": 0}), encoding="utf-8")

    out = _load_counts(p)
    assert out[date(2026, 1, 1)] == 2
    assert out[date(2026, 1, 2)] == 0


def test_load_counts_rejects_non_object(tmp_path: Path) -> None:
    p = tmp_path / "counts.json"
    p.write_text(json.dumps([1, 2, 3]), encoding="utf-8")

    with pytest.raises(ValueError):
        _load_counts(p)
