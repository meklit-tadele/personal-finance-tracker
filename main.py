print("================================")
print("     PERSONAL FINANCE TRACKER")
print("================================")

# Income
income = float(input("Enter your total income: "))

# Expenses
food = float(input("Enter food expenses: "))
transport = float(input("Enter transport expenses: "))
rent = float(input("Enter rent expenses: "))
other = float(input("Enter other expenses: "))

# Calculate total expenses
total_expenses = food + transport + rent + other

# Calculate remaining balance
balance = income - total_expenses

# Display results
print("\n========== FINANCIAL SUMMARY ==========")
print(f"Income: {income:.2f}")
print(f"Food: {food:.2f}")
print(f"Transport: {transport:.2f}")
print(f"Rent: {rent:.2f}")
print(f"Other: {other:.2f}")
print("--------------------------------------")
print(f"Total Expenses: {total_expenses:.2f}")
print(f"Remaining Balance: {balance:.2f}")

# Financial advice
if balance > 0:
    print("\n✅ Great job! You stayed within your budget.")
elif balance == 0:
    print("\n⚠️ You spent exactly what you earned.")
else:
    print("\n❌ Warning! You spent more than your income.")

print("======================================")
