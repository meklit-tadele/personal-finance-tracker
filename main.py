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
    with open("finance_records.txt", "a") as file:
        file.write(f"Income: {income:.2f}\n")
        file.write(f"Expenses: {expenses:.2f}\n")
        file.write(f"Balance: {balance:.2f}\n")
        file.write("--------------------------\n")

    print("\n💾 Record saved successfully!")


def display_summary(income, expenses):
    balance = income - expenses

    print("\n========== FINANCIAL SUMMARY ==========")
    print(f"Income: {income:.2f}")
    print(f"Total Expenses: {expenses:.2f}")
    print(f"Remaining Balance: {balance:.2f}")

    if balance > 0:
        print("✅ Great job! You stayed within your budget.")
    elif balance == 0:
        print("⚠️ You spent exactly what you earned.")
    else:
        print("❌ Warning! You spent more than your income.")

    print("======================================")

    save_record(income, expenses, balance)


# Main program
print("================================")
print("     PERSONAL FINANCE TRACKER")
print("================================")

income = get_income()
expenses = get_expenses()

display_summary(income, expenses)