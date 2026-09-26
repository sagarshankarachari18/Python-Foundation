import os

FILE_NAME = "expenses.txt"

def load_expenses():
    expenses = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, amount = line.rsplit(",", 1)
                    expenses.append({"name": name, "amount": float(amount)})
                except ValueError:
                    continue
    return expenses

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

#Main Program
expenses = load_expenses()
print("---Hello Sagar, Welcome to your Expense Tracker,---")

while True:
    print("\nOptions: 1. Add Expense | 2. show Total | 3. Exit")
    choice = input("choose an option (1-3): ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = get_valid_amount()

        expenses.append({"name": name, "amount": amount})

        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{amount}\n")

        print(f"saved: {name} (€{amount:.2f})")

    elif choice == "2":
        if not expenses:
            print("\nNo Expenses logged yet.")
            continue

        total = sum(item["amount"] for item in expenses)
        for item in expenses:
            print(f" -{item['name']}: €{item['amount']:.2f}")

    elif choice == "3":
        print("Goodbye! Sagar, Happy Saving.")
        break
    else:
        print("Invalid option. Please try again")