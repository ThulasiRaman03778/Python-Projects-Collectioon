import matplotlib.pyplot as plt

expenses = {}

def add_expense(category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def show_expenses():
    for category, amount in expenses.items():
        print(f"{category}: ${amount}")

def plot_expenses():
    categories = list(expenses.keys())
    amounts = list(expenses.values())
    plt.bar(categories, amounts)
    plt.ylabel('Amount ($)')
    plt.title('Personal Expenses')
    plt.show()

if __name__ == "__main__":
    while True:
        action = input("Type 'add' to add expense, 'show' to view expenses, 'plot' to visualize, or 'quit' to exit: ")
        if action == 'add':
            cat = input("Enter expense category: ")
            amt = float(input("Enter amount: "))
            add_expense(cat, amt)
        elif action == 'show':
            show_expenses()
        elif action == 'plot':
            plot_expenses()
        elif action == 'quit':
            break
        else:
            print("Invalid command.")
