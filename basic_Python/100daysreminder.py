from __future__ import annotations

import subprocess
import time
from datetime import datetime, timedelta

TOTAL_DAYS = 100
REMINDER_TIME = "07:00"


def get_day() -> int:
    try:
        with open("day.txt", "r", encoding="utf-8") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 1


def save_day(day: int) -> None:
    with open("day.txt", "w", encoding="utf-8") as f:
        f.write(str(day))


def wait_until_time(target_time: str) -> None:
    now = datetime.now()
    hour, minute = map(int, target_time.split(":", 1))
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

    if target < now:
        target += timedelta(days=1)

    time.sleep((target - now).seconds)


def main() -> None:
    day = get_day()

    while day <= TOTAL_DAYS:
        wait_until_time(REMINDER_TIME)

        message = f"Day {day}/100 – Learn Python today 💻🔥"
        subprocess.run(["notify-send", "100 Days of Code", message], check=False)

        save_day(day)
        day += 1


if __name__ == "__main__":
    main()
