# ==========================================
# PERSONAL FINANCE TRACKER
# Version 4
# ==========================================

def get_income():
    return float(input("Enter your total income: "))


def get_expenses():
    total_expenses = 0

    while True:
        expense = float(input("Enter an expense amount: "))
        total_expenses += expense

        choice = input("Add another expense? (yes/no): ")

        if choice.lower() == "no":
            break

    return total_expenses


def save_record(income, expenses, balance):

    file = open("finance_records.txt", "a")

    file.write(f"Income: {income}\n")
    file.write(f"Expenses: {expenses}\n")
    file.write(f"Balance: {balance}\n")
    file.write("--------------------------\n")

    file.close()


def display_summary(income, expenses):

    balance = income - expenses

    print("\n========== SUMMARY ==========")
    print(f"Income: {income:.2f}")
    print(f"Expenses: {expenses:.2f}")
    print(f"Balance: {balance:.2f}")

    if balance > 0:
        print("✅ Good budgeting!")
    elif balance == 0:
        print("⚠️ You spent everything.")
    else:
        print("❌ You spent more than you earned.")

    save_record(income, expenses, balance)


print("================================")
print("     PERSONAL FINANCE TRACKER")
print("================================")

income = get_income()
expenses = get_expenses()

display_summary(income, expenses)
