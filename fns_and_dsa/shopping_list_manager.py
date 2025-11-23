def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if choice == 1:
            item = input("Add item to your shopping list: ")
            shopping_list.append(item)
            print(f"'{item}' added!\n")

        elif choice == 2:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed!\n")
            else:
                print("This item cannot be found in your list\n")

        elif choice == 3:
            if not shopping_list:
                print("Your shopping list is empty.\n")
            else:
                print("Current List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print()

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
