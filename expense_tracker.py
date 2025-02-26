expenses = []

def display_menu():
    menu = """
        Welcome to Semicolon Expense Tracker App
        --------------------------------------
        
        1. Add an expense
        2. View all expenses
        3. Calculate total expenses
        4. Exit
        
    """
    return menu

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("Invalid input. Amount must be greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    expense = {'date': date, 'description': description, 'amount': amount}
    expenses.append(expense)
    return "Expense added successfully!"

def display_all_expenses():
    if not expenses:
        return "No expenses recorded yet."
    else:
        expense_list = []
        for expense in expenses:
            expense_list.append(f"Date: {expense['date']}, Description: {expense['description']}, Amount: {expense['amount']}")
        return "\n".join(expense_list)

def calculate_total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    return f"Total Expenses: {total}"

def exit_application():
    return "Exiting the application. Goodbye!"

def main():
    while True:
        print(display_menu())
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            result = add_expense()
            print(result)
        
        elif choice == '2':
            result = display_all_expenses()
            print(result)
        
        elif choice == '3':
            result = calculate_total_expenses()
            print(result)
        
        elif choice == '4':
            result = exit_application()
            print(result)
            break
        
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
