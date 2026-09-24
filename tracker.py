import os

FILE_NAME = r"D:\GitHub-Projects\Python_foundation\expenses.txt"

expenses = []
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r")as file:
        for line in file:
            if not line.strip():
                continue
            name, amount = line.strip().split(",")
            expenses.append({"name": name, "amount": float(amount)})

print("---Hello Sagar, Welcome to your Expense Tracker,---")

while True:
    print("\nOptions: 1. Add Expense | 2. show Total | 3. Exit")
    choice = input("choose an option (1-3): ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount €: "))
        expenses.append({"name": name, "amount": amount})

        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{amount}\n")

        print(f"saved: {name} (€{amount})")

    elif choice == "2":
        total = sum(item["amount"]for item in expenses)
        print(f"\n Total Expenses: €{total: .2f}")
        for item in expenses:
            print(f" -{item['name']}: €{item['amount']: .2f}")

    elif choice == "3":
        print("Goodbye! Sagar, Happy Saving.")
        break
    else:
        print("Invalid option. Please try again")