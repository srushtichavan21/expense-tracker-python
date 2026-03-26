import json
import os

FILE = "expenses.json"

def load():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(data):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    data.append({
        "name": name,
        "amount": amount,
        "category": category
    })

    save(data)
    print("✅ Expense added!")

def view_expenses(data):
    total = 0
    print("\n--- Expenses ---")
    for exp in data:
        print(f"{exp['name']} - ₹{exp['amount']} ({exp['category']})")
        total += exp['amount']

    print(f"\nTotal Spending: ₹{total}")

def main():
    data = load()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_expenses(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()