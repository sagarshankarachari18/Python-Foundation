expenses = []

print("---Hello Sagar, Welcome Back,---")

while True:
    print("\nOptions: 1. Add Expense | 2. show Total | 3. Exit")
    choice = input("choose an option (1-3): ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount €: "))
        expenses.append({"name": name, "amount": amount})
        print(f"Added: {name} (€{amount})")

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