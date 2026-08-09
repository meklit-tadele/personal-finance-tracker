print("================================")
print("     PERSONAL FINANCE TRACKER")
print("================================")

income = float(input("Enter your total income: "))
expenses = float(input("Enter your total expenses: "))

balance = income - expenses

print("\n----- Financial Summary -----")
print(f"Income: {income:.2f}")
print(f"Expenses: {expenses:.2f}")
print(f"Remaining Balance: {balance:.2f}")
