"""Simple streak CLI: store quick notes/check-ins in a local JSON file.

Usage:
  python -m streak_cli
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.json"


@dataclass
class Note:
    ts: str
    text: str


def _load() -> list[dict]:
    if not DATA_PATH.exists():
        return []
    try:
        return json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except Exception:
        return []


def _save(items: list[dict]) -> None:
    DATA_PATH.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def add_note(text: str) -> None:
    items = _load()
    items.append({"ts": datetime.now().isoformat(timespec="seconds"), "text": text.strip()})
    _save(items)


def list_notes(limit: int = 20) -> list[Note]:
    items = _load()
    sliced = items[-limit:]
    return [Note(ts=i.get("ts", ""), text=i.get("text", "")) for i in sliced]


def main() -> int:
    print("streak_cli — quick notes for 2026 streak")
    print("1) Add note")
    print("2) List notes")
    choice = input("> ").strip()

    if choice == "1":
        text = input("note: ").strip()
        if not text:
            print("No note entered.")
            return 1
        add_note(text)
        print("Saved.")
        return 0

    if choice == "2":
        notes = list_notes()
        if not notes:
            print("No notes yet.")
            return 0
        for n in notes:
            print(f"- {n.ts}: {n.text}")
        return 0

    print("Unknown option.")
    return 1
