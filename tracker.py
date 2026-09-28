import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    """Load expense list from a JSON file."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, ValueError):
            return []
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount €: "))
            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid numerical amount.")

# Main Program
expenses = load_expenses()
print("--- Hello Sagar, Welcome to your Expense Tracker ---")

while True:
    print("\nOptions: 1. Add Expense | 2. Show Total | 3. Exit")
    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        name = input("Enter expense name: ").strip()
        amount = get_valid_amount()

        expenses.append({"name": name, "amount": amount})
        save_expenses(expenses)

        print(f"Saved: {name} (€{amount:.2f})")

    elif choice == "2":
        if not expenses:
            print("\nNo expenses logged yet.")
            continue

        total = sum(item["amount"] for item in expenses)
        print(f"\nTotal Expenses: €{total:.2f}")
        for item in expenses:
            print(f" - {item['name']}: €{item['amount']:.2f}")

    elif choice == "3":
        print("Goodbye Sagar! Happy Saving.")
        break
    else:
        print("Invalid option. Please try again.")