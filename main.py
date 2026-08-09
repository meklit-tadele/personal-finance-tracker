# ==========================================
# PERSONAL FINANCE TRACKER
# Version 3
# ==========================================

def get_income():
    return float(input("Enter your total income: "))


def get_expenses():

    total_expenses = 0

    while True:

        expense = float(input("Enter an expense amount: "))

        total_expenses += expense

        choice = input("Do you want to add another expense? (yes/no): ")

        if choice.lower() == "no":
            break

    return total_expenses


def display_summary(income, total_expenses):

    balance = income - total_expenses

    print("\n========== FINANCIAL SUMMARY ==========")
    print(f"Income: {income:.2f}")
    print(f"Total Expenses: {total_expenses:.2f}")
    print(f"Remaining Balance: {balance:.2f}")

    if balance > 0:
        print("✅ Great job! You stayed within your budget.")
    elif balance == 0:
        print("⚠️ You spent exactly what you earned.")
    else:
        print("❌ Warning! You spent more than your income.")

    print("======================================")


print("================================")
print("     PERSONAL FINANCE TRACKER")
print("================================")

income = get_income()

total_expenses = get_expenses()

display_summary(income, total_expenses)
