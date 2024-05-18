class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description=""):
        """
        Adds a new expense to the tracker.
        
        :param amount: float, the amount of the expense
        :param category: str, the category of the expense
        :param description: str, a description of the expense (optional)
        """
        self.expenses.append({
            'amount': amount,
            'category': category,
            'description': description
        })
        print(f"Added expense: {amount} in category: {category}")

    def get_total_expense(self):
        """
        Returns the total amount of all expenses.
        
        :return: float, total amount of expenses
        """
        return sum(expense['amount'] for expense in self.expenses)

    def get_expenses_by_category(self):
        """
        Returns a dictionary with total expenses per category.
        
        :return: dict, category-wise expense totals
        """
        category_totals = {}
        for expense in self.expenses:
            category = expense['category']
            if category in category_totals:
                category_totals[category] += expense['amount']
            else:
                category_totals[category] = expense['amount']
        return category_totals

    def print_summary(self):
        """
        Prints a summary of expenses including total and by category.
        """
        total = self.get_total_expense()
        print(f"Total Expense: {total:.2f}")
        category_totals = self.get_expenses_by_category()
        print("Expenses by Category:")
        for category, total in category_totals.items():
            print(f"  {category}: {total:.2f}")


if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description (optional): ")
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("Invalid input. Please enter a numerical value for the amount.")
        elif choice == "2":
            tracker.print_summary()
        elif choice == "3":
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")
