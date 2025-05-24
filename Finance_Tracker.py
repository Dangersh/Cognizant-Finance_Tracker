# Dictionary to store expenses, organized by category
expenses_by_category = {}  # Global dictionary to store expenses

def print_welcome():
    print("Welcome to the Personal Finance Tracker!")

# Function to display the main menu and handle user choices
def main_menu():
    while True:
        print("\nWhat would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")
        try:
            choice = int(input("Choose an option: "))  # Prompt user for a menu option
            if choice == 1:
                add_expense()  # Call function to add an expense
            elif choice == 2:
                view_expenses(expenses_by_category)  # Call function to view all expenses
            elif choice == 3:
                view_summary(expenses_by_category)  # Call function to view summary
            elif choice == 4:
                print("Goodbye!")  
                break  
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")  # Handle invalid menu option
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle non-integer input

# Function to add a new expense entry
def add_expense():
    while True:
        try:
            
            description = input("Enter expense description: ").strip()
            if not description:
                raise ValueError("Description cannot be empty.")

      
            category = input("Enter category: ").strip()
            if not category:
                raise ValueError("Category cannot be empty.")

            # Prompt for expense amount and convert to float
            amount_input = input("Enter amount: ").strip()
            amount = float(amount_input)
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
        
        # Handle input validation and type conversion errors
        except ValueError as e:
            if 'could not convert string to float' in str(e):
                print("Invalid amount. Please enter a number.")  
            else:
                print(f"Invalid input: {e}")  # General input error
            continue  
        except KeyboardInterrupt:
            print("\nInput cancelled.")  
            return  
        except Exception as e:
            print(f"Unexpected error: {e}")  # Catch-all for unexpected errors
            return  
        else:
            # Prepare expense tuple
            expense = (description, amount)

            # Add expense to the appropriate category
            if category not in expenses_by_category:
                expenses_by_category[category] = []  # Create new category list if it doesn't exist
            expenses_by_category[category].append(expense)  # Append expense to category list
            print("Expense added successfully.")  
            break  

# Function to view all recorded expenses
def view_expenses(data):
    if not data:
        print("No expenses recorded yet.")  # Handle case with no data
        return
    for category, expenses in data.items():
        print(f"\nCategory: {category}")  # Print category name
        for desc, amt in expenses:
            print(f"  - {desc}: ${amt:.2f}")  

# Function to display a summary of total expenses per category
def view_summary(data):
    if not data:
        print("No expenses recorded yet.")  # Handle case with no data
        return
    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)  
        print(f"{category}: ${total:.2f}")  

# Entry point of the program
if __name__ == "__main__":
    print_welcome()  
    main_menu()     
