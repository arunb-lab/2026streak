import time
import subprocess
from datetime import datetime, timedelta

TOTAL_DAYS = 100
REMINDER_TIME = "07:00"

def get_day():
    try:
        with open("day.txt", "r") as f:
            return int(f.read())
    except:
        return 1

def save_day(day):
    with open("day.txt", "w") as f:
        f.write(str(day))

def wait_until_time(target_time):
    now = datetime.now()
    hour, minute = map(int, target_time.split(":"))
    target = now.replace(hour=hour, minute=minute, second=0)

    if target < now:
        target += timedelta(days=1)

    time.sleep((target - now).seconds)

day = get_day()

while day <= TOTAL_DAYS:
    wait_until_time(REMINDER_TIME)

    message = f"Day {day}/100 – Learn Python today 💻🔥"
    subprocess.run(["notify-send", "100 Days of Code", message])

    save_day(day)
    day += 1
