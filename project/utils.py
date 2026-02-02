import json
import time

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def suggest_task(tasks):
    pending = [t for t in tasks if not t["done"]]

    if not pending:
        print("Nothing left. Touch grass 🌱")
        return

    easiest = min(pending, key=lambda t: t["time_spent"])
    print(f"Suggested task: {easiest['name']}")
