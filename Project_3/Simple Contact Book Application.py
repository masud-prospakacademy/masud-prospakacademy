
contacts = {} 

def display_menu(): 
    print("\n--- Contact Book Menu ---") 
    print("1. Add/Update Contact") 
    print("2. View Contact") 
    print("3. List All Contacts") 
    print("4. Delete Contact") 
    print("5. Exit") 
    print("-------------------------") 

def add_contact(): 
    name = input("Enter contact name: ").strip().title() 
    
    if name in contacts: 
        print(f"Contact '{name}' already exists.") 
        confirm = input("Do you want to update their details? (yes/no): ").lower() 
        if confirm != 'yes': 
            print("Action cancelled.") 
            return 
 
    phone = input("Enter phone number: ").strip() 
    email = input("Enter email address: ").strip() 
    
    contacts[name] = {"phone": phone, "email": email} 
    print(f"Contact '{name}' saved successfully.") 

def view_contact(): 
    name = input("Enter contact name to view: ").strip().title() 
    if name in contacts: 
        details = contacts[name] 
        print(f"\n--- {name} ---") 
        print(f"Phone: {details['phone']}") 
        print(f"Email: {details['email']}") 
    else: 
        print(f"Error: '{name}' not found.") 

def list_all_contacts(): 
    if not contacts: 
        print("Your contact book is empty.") 
        return 
 
    print("\n--- All Contacts ---") 
    for name, details in contacts.items(): 
        print(f"{name:.<20} {details['phone']}") 

def delete_contact(): 
    name = input("Enter contact name to delete: ").strip().title() 
    if name in contacts: 
        del contacts[name] 
        print(f"Contact '{name}' removed.") 
    else: 
        print(f"Error: '{name}' not found.") 

def main(): 
    while True: 
        display_menu() 
        choice = input("Enter choice (1-5): ").strip() 
 
        if choice == '1': 
            add_contact() 
        elif choice == '2': 
            view_contact() 
        elif choice == '3': 
            list_all_contacts() 
        elif choice == '4': 
            delete_contact() 
        elif choice == '5': 
            print("Closing application. Goodbye!") 
            break 
        else: 
            print("Invalid selection. Please try again.") 

if __name__ == "__main__": 
    main()