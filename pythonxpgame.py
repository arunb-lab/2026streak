import json
from datetime import date

FILE = "xp_data.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {"xp": 0, "logs": []}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

data = load_data()
today = str(date.today())

print("\n🎯 PYTHON XP SYSTEM")
print("1. Read / Watch Python content (+5 XP)")
print("2. Solve a problem (+15 XP)")
print("3. Write a script (+25 XP)")
print("4. Build something real (+40 XP)")
print("5. Teach / Post / Explain (+50 XP)")

choice = input("\nChoose activity (1–5): ").strip()

xp_map = {
    "1": 5,
    "2": 15,
    "3": 25,
    "4": 40,
    "5": 50
}

if choice not in xp_map:
    print("❌ Invalid choice. No XP today.")
    exit()

note = input("What did you do? → ").strip()

earned = xp_map[choice]
data["xp"] += earned
data["logs"].append(f"{today} | +{earned} XP | {note}")

level = data["xp"] // 100 + 1

save_data(data)

print(f"\n⚡ +{earned} XP earned")
print(f"🏆 Level {level}")
print(f"🔥 Total XP: {data['xp']}")
