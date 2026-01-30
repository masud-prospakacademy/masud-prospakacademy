import datetime

NOTES_FILE = "my_diary_notes.txt"

def add_note():
    """Captures a note and appends it to the file with a timestamp."""
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note_content = input("Enter your diary entry: ")

    with open(NOTES_FILE, "a") as file:
        file.write(f"[{timestamp}] {note_content}\n")
    
    print("Note added successfully!")

def view_notes():
    """Reads and displays all entries from the diary file."""
    try:
        with open(NOTES_FILE, "r") as file:
            print("\n--- Your Diary Entries ---")
            for line in file:
                print(line.strip())
            print("--------------------------")
    except FileNotFoundError:
        print("\nNo diary entries found yet. Start by adding one!")

def main():
    """Main menu loop to drive the application."""
    while True:
        print("\n--- Diary App Menu ---")
        print("1. Add a new note")
        print("2. View all notes")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            print("Exiting Diary App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()