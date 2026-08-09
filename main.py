# ==========================================
# PERSONAL FINANCE TRACKER
# Version 2
# ==========================================

def get_income():
    return float(input("Enter your total income: "))


def get_expenses():
    food = float(input("Enter food expenses: "))
    transport = float(input("Enter transport expenses: "))
    rent = float(input("Enter rent expenses: "))
    other = float(input("Enter other expenses: "))

    total_expenses = food + transport + rent + other

    return food, transport, rent, other, total_expenses


def display_summary(income, food, transport, rent, other, total_expenses):

    balance = income - total_expenses

    print("\n========== FINANCIAL SUMMARY ==========")
    print(f"Income: {income:.2f}")
    print(f"Food: {food:.2f}")
    print(f"Transport: {transport:.2f}")
    print(f"Rent: {rent:.2f}")
    print(f"Other: {other:.2f}")
    print("--------------------------------------")
    print(f"Total Expenses: {total_expenses:.2f}")
    print(f"Remaining Balance: {balance:.2f}")

    if balance > 0:
        print("\n✅ Great job! You stayed within your budget.")
    elif balance == 0:
        print("\n⚠️ You spent exactly what you earned.")
    else:
        print("\n❌ Warning! You spent more than your income.")

    print("======================================")


print("================================")
print("     PERSONAL FINANCE TRACKER")
print("================================")

income = get_income()

food, transport, rent, other, total_expenses = get_expenses()

display_summary(
    income,
    food,
    transport,
    rent,
    other,
    total_expenses
)
