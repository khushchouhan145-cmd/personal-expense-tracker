"""
=============================================================================
Day 1: Python Fundamentals Practice
Author: Khushi
Topics Covered:
  1. Variables, Data Types, Type Casting & Operators
  2. Input / Output & String Formatting
  3. Conditional Statements (if-elif-else)
  4. Loops (for & while)
  5. Lists & Dictionaries (Expense Data Representation)
  6. Functions & Reusability
=============================================================================
"""

print("=== DAY 1: PYTHON BASICS PRACTICE FOR EXPENSE TRACKER ===\n")

# ---------------------------------------------------------------------------
# 1. Variables, Data Types & Type Casting
# ---------------------------------------------------------------------------
print("--- 1. Variables & Types ---")
expense_title = "College Books"     # String (str)
expense_amount = 450.50             # Float (float)
is_essential = True                 # Boolean (bool)
transaction_id = 101                # Integer (int)

print(f"Title: {expense_title} (Type: {type(expense_title).__name__})")
print(f"Amount: Rs. {expense_amount} (Type: {type(expense_amount).__name__})")
print(f"Essential: {is_essential} (Type: {type(is_essential).__name__})\n")


# ---------------------------------------------------------------------------
# 2. Operators & Calculations
# ---------------------------------------------------------------------------
print("--- 2. Operators & Calculations ---")
monthly_budget = 5000.0
total_spent = expense_amount + 250.0 + 1200.0  # Arithmetic operators
remaining_balance = monthly_budget - total_spent

print(f"Monthly Budget: Rs. {monthly_budget}")
print(f"Total Spent:    Rs. {total_spent}")
print(f"Remaining:      Rs. {remaining_balance}\n")


# ---------------------------------------------------------------------------
# 3. Conditional Statements (Budget Warning)
# ---------------------------------------------------------------------------
print("--- 3. Conditional Statements (Budget Check) ---")
if total_spent > monthly_budget:
    print("[ALERT] You have exceeded your monthly budget!")
elif total_spent >= (monthly_budget * 0.8):
    print("[WARNING] You have used more than 80% of your budget.")
else:
    print("[OK] Spending is well within your budget.\n")


# ---------------------------------------------------------------------------
# 4. Lists & Loops (Tracking Multiple Items)
# ---------------------------------------------------------------------------
print("--- 4. Lists & For Loops ---")
categories = ["Food", "Travel", "Shopping", "Education", "Bills", "Healthcare", "Others"]

print("Available Expense Categories:")
for index, cat in enumerate(categories, start=1):
    print(f"  {index}. {cat}")
print()


# ---------------------------------------------------------------------------
# 5. Dictionaries: Representing a Single Expense Record
# ---------------------------------------------------------------------------
print("--- 5. Dictionary (Core Project Data Structure) ---")
sample_expense = {
    "id": 1,
    "date": "2026-10-21",
    "title": "Bus Pass",
    "amount": 350.0,
    "category": "Travel"
}

print("Sample Expense Record:")
for key, value in sample_expense.items():
    print(f"  {key.capitalize()}: {value}")
print()


# ---------------------------------------------------------------------------
# 6. Functions: Modular Calculations
# ---------------------------------------------------------------------------
print("--- 6. Functions & List of Dictionaries ---")

# A list containing multiple expense dictionaries
daily_expenses = [
    {"title": "Morning Tea & Snacks", "amount": 60.0, "category": "Food"},
    {"title": "Metro Recharge", "amount": 200.0, "category": "Travel"},
    {"title": "Notebooks", "amount": 140.0, "category": "Education"}
]

def calculate_total_expenses(expense_list):
    """Calculates and returns the sum of all expenses in the list."""
    total = 0.0
    for item in expense_list:
        total += item["amount"]
    return total

calculated_total = calculate_total_expenses(daily_expenses)
print(f"Total calculated by function: Rs. {calculated_total:.2f}")

print("\n=== DAY 1 PRACTICE COMPLETED SUCCESSFULLY! ===")
