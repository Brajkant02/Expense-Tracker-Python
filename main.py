import json
from datetime import date

FILE_NAME = "expenses.json"


# Load Expenses
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Save Expenses
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add Expense
def add_expense(expenses):
    category = input("Enter Category: ").strip().title()

    if not category:
        print("Category cannot be empty!")
        return

    try:
        amount = float(input("Enter Amount: "))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

    except ValueError:
        print("Please enter a valid number!")
        return

    expense = {
        "date": str(date.today()),
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


# View Expenses
def view_expenses(expenses):

    if not expenses:
        print("No expenses found!")
        return

    print("\n----- All Expenses -----")

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense.get('date', 'N/A')} | "
              f"{expense['category']} | ₹{expense['amount']:.2f}")

    print("------------------------")


# Delete Expense
def delete_expense(expenses):

    if not expenses:
        print("No expenses to delete!")
        return

    view_expenses(expenses)

    try:
        number = int(input("Enter the number to delete: "))

        if number < 1 or number > len(expenses):
            print("Number not in the list!")
            return

    except ValueError:
        print("Please enter a valid number!")
        return

    removed = expenses.pop(number - 1)
    save_expenses(expenses)

    print(f"Deleted: {removed['category']} - ₹{removed['amount']:.2f}")


# Category Wise Total
def category_total(expenses):

    if not expenses:
        print("No expenses found!")
        return

    total = {}
    grand_total = 0

    for expense in expenses:

        category = expense["category"].strip().title()
        amount = float(expense["amount"])

        total[category] = total.get(category, 0) + amount
        grand_total += amount

    print("\n----- Category Wise Total -----")

    for category, amount in total.items():
        print(f"{category}: ₹{amount:.2f}")

    print("-------------------------------")
    print(f"Grand Total: ₹{grand_total:.2f}")


# Main Menu
def main():
    expenses = load_expenses()

    while True:

        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Category Total")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            delete_expense(expenses)

        elif choice == "4":
            category_total(expenses)

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
