from datetime import date

from expense import Expense


def main():
    print(f"Running Expense Tracking")

    expense_file_name = r"Expense Tracker.CSV"
    budget = 2000
    # Get user input expense
    expense = get_user_expense()

    # Write their expense into a file
    write_expense_to_file(expense, expense_file_name)
    # Read file and summarize expenses
    read_summarize_expense(expense_file_name,budget)


def get_user_expense():
    print(f"Running Expense Tracking 2")
    expense_name = input("Enter expense name here: ")
    expense_amount = float(input("Enter expense amount here: "))
    print(f"{expense_name}, cost {expense_amount}")
    expense_category = [
        "Food", "Shopping", "Bill & Fee", "Investment"]
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_category):
            print(f"   {i+1}. {category_name}")
        value_range = f"[1 - {len(category_name)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) -1

        if i in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print(f"Invalid value inserted")
        break

def write_expense_to_file(expense, expense_file_name):
    print(f"Running Expense Tracking 3")
    with open(expense_file_name, 'a') as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")


def read_summarize_expense(expense_file_name,budget):
    expenses: list[Expense] = []
    with open(expense_file_name, 'r') as f:
        lines = f.readlines()

        for line in lines:
            expense_name, expense_category, expense_amount= line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                category=expense_category,
                amount=float(expense_amount),
                )
            expenses.append(line_expense)

    amount_by_category = {}

    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expense by category:")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")

    total_spent = sum([ex.amount for ex in expenses])
    print(f"You haven spent total of ${total_spent:.2f} this month")

    remaining_budget = budget - total_spent
    print(f"Your total balance is ${remaining_budget} as of {date.today()} ")
if __name__ == "__main__":
    main()
