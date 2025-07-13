from timer import start_pomodoro

def show_menu():
    print("\n=== Pomodoro Timer ===")
    print("1. Start Pomodoro Session")
    print("2. Quit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            start_pomodoro()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
