expenses_by_category = {}  # Global dictionary to store expenses

def print_welcome():
    print("Welcome to the Personal Finance Tracker!")

def main_menu():
    while True:
        print("\nWhat would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses(expenses_by_category)
            elif choice == 3:
                view_summary(expenses_by_category)
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_expense():
    while True:
        try:
            description = input("Enter expense description: ").strip()
            if not description:
                raise ValueError("Description cannot be empty.")

            category = input("Enter category: ").strip()
            if not category:
                raise ValueError("Category cannot be empty.")

            amount_input = input("Enter amount: ").strip()
            amount = float(amount_input)
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
        
        except ValueError as e:
            if 'could not convert string to float' in str(e):
                print("Invalid amount. Please enter a number.")
            else:
                print(f"Invalid input: {e}")
            continue
        except KeyboardInterrupt:
            print("\nInput cancelled.")
            return
        except Exception as e:
            print(f"Unexpected error: {e}")
            return
        else:
            expense = (description, amount)
            if category not in expenses_by_category:
                expenses_by_category[category] = []
            expenses_by_category[category].append(expense)
            print("Expense added successfully.")
            break

def view_expenses(data):
    if not data:
        print("No expenses recorded yet.")
        return
    for category, expenses in data.items():
        print(f"\nCategory: {category}")
        for desc, amt in expenses:
            print(f"  - {desc}: ${amt:.2f}")

def view_summary(data):
    if not data:
        print("No expenses recorded yet.")
        return
    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")

# Run the program
if __name__ == "__main__":
    print_welcome()
    main_menu()
