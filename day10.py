import time
from datetime import datetime

def show_date_time():
    now = datetime.now()
    print("\nCurrent Date & Time:")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def timer():
    seconds = int(input("\nEnter time in seconds: "))
    print("Timer started...")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")

def stopwatch():
    print("\nStopwatch started. Press Ctrl + C to stop.")
    start = time.time()
    try:
        while True:
            elapsed = time.time() - start
            mins, secs = divmod(int(elapsed), 60)
            print(f"{mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")

while True:
    print("""
1. Show Date & Time
2. Timer
3. Stopwatch
4. Exit
""")
    choice = input("Choose an option: ")

    if choice == "1":
        show_date_time()
    elif choice == "2":
        timer()
    elif choice == "3":
        stopwatch()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
