import json
import os
import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = ["Food", "Transportation", "Entertainment", "Utilities", "Shopping", "Other"]
        self.data_file = "expenses.json"
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.expenses = json.load(file)

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        today = datetime.date.today().strftime("%Y-%m-%d")
        self.expenses.append({
            'date': today,
            'amount': amount,
            'category': category,
            'description': description
        })
        self.save_data()

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            for expense in self.expenses:
                print(f"Date: {expense['date']}")
                print(f"Amount: ${expense['amount']}")
                print(f"Category: {expense['category']}")
                print(f"Description: {expense['description']}")
                print()

    def monthly_summary(self):
        monthly_expenses = {}
        for expense in self.expenses:
            date = expense['date']
            month = date.split('-')[1]
            if month not in monthly_expenses:
                monthly_expenses[month] = 0
            monthly_expenses[month] += expense['amount']
        
        print("Monthly Summary:")
        for month, amount in monthly_expenses.items():
            print(f"{datetime.datetime.strptime(month, '%m').strftime('%B')}: ${amount}")

    def category_summary(self):
        category_expenses = {category: 0 for category in self.categories}
        for expense in self.expenses:
            category_expenses[expense['category']] += expense['amount']
        
        print("Category-wise Summary:")
        for category, amount in category_expenses.items():
            print(f"{category}: ${amount}")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category-wise Summary")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input(f"Enter category ({', '.join(tracker.categories)}): ").capitalize()
            description = input("Enter description: ")
            if category not in tracker.categories:
                print("Invalid category!")
                continue
            tracker.add_expense(amount, category, description)
            print("Expense added successfully!")
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.monthly_summary()
        elif choice == '4':
            tracker.category_summary()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
