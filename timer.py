import time
import json
from datetime import datetime
from playsound import playsound
import os

CONFIG_FILE = "config.json"

def countdown(minutes, label):
    seconds = minutes * 60
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer = f"{label} - {mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print(f"\n⏰ {label} session ended!")

def play_sound():
    try:
        playsound("alarm.wav")
    except:
        print("🔇 Sound failed. Make sure 'alarm.wav' is in the folder.")

def log_session(round_num, work_duration):
    now = datetime.now()
    log_entry = f"{now.strftime('%Y-%m-%d %H:%M:%S')} - Pomodoro Round {round_num} - {work_duration} mins focused\n"
    with open("focus_history.txt", "a") as file:
        file.write(log_entry)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return None

def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file)

def choose_timer_settings():
    print("\n📋 Choose Timer Settings:")
    print("1. Classic (25m work / 5m break / 4 rounds)")
    print("2. Long Work (50m work / 10m break / 2 rounds)")
    print("3. Custom")
    print("4. Use Saved Default")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        return {"work": 25, "break": 5, "rounds": 4}
    elif choice == "2":
        return {"work": 50, "break": 10, "rounds": 2}
    elif choice == "3":
        work = int(input("Enter work duration in minutes: "))
        brk = int(input("Enter break duration in minutes: "))
        rounds = int(input("Enter number of Pomodoro rounds: "))
        save = input("Save as default? (y/n): ").lower()
        config = {"work": work, "break": brk, "rounds": rounds}
        if save == "y":
            save_config(config)
        return config
    elif choice == "4":
        config = load_config()
        if config:
            print("✅ Loaded saved config!")
            return config
        else:
            print("❌ No saved config found. Using Classic.")
            return {"work": 25, "break": 5, "rounds": 4}
    else:
        print("Invalid choice. Using Classic.")
        return {"work": 25, "break": 5, "rounds": 4}

def start_pomodoro():
    try:
        config = choose_timer_settings()
        work_duration = config["work"]
        break_duration = config["break"]
        rounds = config["rounds"]

        for i in range(1, rounds + 1):
            print(f"\n🍅 Pomodoro Round {i} - Time to focus!")
            countdown(work_duration, "Work")
            play_sound()
            log_session(i, work_duration)

            if i < rounds:
                print("🛌 Break Time!")
                countdown(break_duration, "Break")
                play_sound()

        print("\n🎉 All Pomodoro rounds completed!")

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
