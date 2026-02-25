# budget_calculator.py - Personal Finance Calculator
# Starter code for e002-exercise-python-intro

"""
Personal Finance Calculator
---------------------------
This program helps users understand their monthly budget by collecting
income and expense information and displaying a formatted summary.

Complete the TODO sections below to finish the program.
"""

print("=" * 44)
print("       PERSONAL FINANCE CALCULATOR")
print("=" * 44)
print()

# =============================================================================
# TODO: Task 1 - Collect User Information
# =============================================================================
# Get the user's name
# Example: name = input("Enter your name: ")
name = input("Enter name: ")
if (name == ""):
    name = "Anonymous"

# Get monthly income (as a float)
# Remember to convert the input to a float!
income = float(input("Enter monthly income: "))
if (income <= 0):
    print("ERROR: Negative income reported. Exitting program...")
    quit()

# Get expenses for at least 4 categories:
# - rent: Rent/Housing
# - utilities: Utilities (electric, water, internet)
# - food: Food/Groceries
# - transportation: Transportation (gas, public transit)
print("Enter monthly costs for the following")
rent = max(float(input("Rent: ")), 0.0)
utilities = max(float(input("Utilities: ")), 0.0)
food = max(float(input("Food: ")), 0.0)
transportation = max(float(input("Transportation: ")), 0.0)

# =============================================================================
# TODO: Task 2 - Perform Calculations
# =============================================================================
# Calculate total expenses
expenses = rent + utilities + food + transportation

# Calculate remaining balance (income - expenses)
balance = income - expenses

# Calculate savings rate as a percentage
# Formula: (balance / income) * 100
savings_rate = (balance / income) * 100

# Determine financial status
# - If balance > 0: status = "in the green"
# - If balance < 0: status = "in the red"
# - If balance == 0: status = "breaking even"
if (balance > 0):
    status = "in the green"
elif (balance < 0):
    status = "in the red"
else:
    status = "breaking even"

# =============================================================================
# TODO: Task 3 - Display Results
# =============================================================================
# Create a formatted budget report
# Use f-strings for formatting
# Dollar amounts should show 2 decimal places: f"${amount:.2f}"
# Percentages should show 1 decimal place: f"{rate:.1f}%"

# Example structure:
# print("=" * 44)
# print("       MONTHLY BUDGET REPORT")
# print("=" * 44)
# print(f"Name: {name}")
# ... continue building the report ...

print("=" * 44)
print("     MONTHLY BUDGET REPORT")
print("=" * 44)
print(f"Name: {name}\n")
print(f"Income: ${income:.2f}\n")
print("=" * 22)
print("     EXPENSES")
print("=" * 22)
print(f"Rent: ${rent:.2f} - {(rent / income) * 100:.2f}% of income")
print(f"Utilities: ${utilities:.2f} - {(utilities / income) * 100:.2f}% of income")
print(f"Food: ${food:.2f} - {(food / income) * 100:.2f}% of income")
print(f"Transportation: ${transportation:.2f} - {(transportation / income) * 100:.2f}% of income")
print("-" * 10)
print(f"Total Expenses: ${expenses:.2f}\n")
print(f"Final Balance: ${balance:.2f}")
print(f"Savings Rate: ~{savings_rate:.2f}%")
print(f"Status: {status}")

# =============================================================================
# TODO: Task 4 - Add Validation (Optional Enhancement)
# =============================================================================
# Add these validations before calculations:
# - If name is empty, use "Anonymous"
# - If income is <= 0, print error and exit
# - If any expense is negative, treat as 0


# =============================================================================
# STRETCH GOAL: Category Percentages
# =============================================================================
# Add a section showing what percentage each expense is of total income
# Example: print(f"  - Rent/Housing:    {(rent/income)*100:.1f}% of income")
