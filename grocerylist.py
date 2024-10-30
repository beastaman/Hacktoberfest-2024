import json
import os

# File to store the grocery list
GROCERY_FILE = 'grocery_list.json'

# Load the grocery list from file
def load_grocery_list():
    if os.path.exists(GROCERY_FILE):
        with open(GROCERY_FILE, 'r') as file:
            return json.load(file)
    return []

# Save the grocery list to file
def save_grocery_list(grocery_list):
    with open(GROCERY_FILE, 'w') as file:
        json.dump(grocery_list, file, indent=4)

# Add item to the grocery list
def add_item(item):
    grocery_list.append({"item": item, "bought": False})
    save_grocery_list(grocery_list)
    print(f'Added "{item}" to the grocery list.')

# View all items in the grocery list
def view_list():
    print("\nGrocery List:")
    for index, item in enumerate(grocery_list, start=1):
        status = "Bought" if item["bought"] else "Not bought"
        print(f'{index}. {item["item"]} - {status}')
    print()

# Mark an item as bought
def mark_as_bought(index):
    if 0 <= index < len(grocery_list):
        grocery_list[index]["bought"] = True
        save_grocery_list(grocery_list)
        print(f'Marked "{grocery_list[index]["item"]}" as bought.')
    else:
        print("Invalid item number.")

# Remove an item from the grocery list
def remove_item(index):
    if 0 <= index < len(grocery_list):
        removed_item = grocery_list.pop(index)
        save_grocery_list(grocery_list)
        print(f'Removed "{removed_item["item"]}" from the grocery list.')
    else:
        print("Invalid item number.")

# Command line interface
def main():
    while True:
        print("\n--- Grocery List Menu ---")
        print("1. Add an item")
        print("2. View grocery list")
        print("3. Mark item as bought")
        print("4. Remove an item")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        
        elif choice == '2':
            view_list()
        
        elif choice == '3':
            try:
                index = int(input("Enter item number to mark as bought: ")) - 1
                mark_as_bought(index)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '4':
            try:
                index = int(input("Enter item number to remove: ")) - 1
                remove_item(index)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Load grocery list and run the main menu
if __name__ == '__main__':
    grocery_list = load_grocery_list()
    main()
