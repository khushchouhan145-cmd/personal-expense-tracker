"""
Personal Expense Tracker
Author: Internship Project
Description: A complete console application to record, view, search, 
             analyze, and manage daily expenses using CSV storage.
"""

import csv
import os
from datetime import datetime

# CSV file path where our expenses are permanently stored
FILE_NAME = "expenses.csv"

# Pre-defined categories required for the project
CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Education",
    "Bills",
    "Healthcare",
    "Others"
]


def load_expenses():
    """
    Reads all expenses from the CSV file and returns them as a list of dictionaries.
    If the file does not exist, it creates a new one with header columns.
    """
    expenses = []
    
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "date", "title", "amount", "category"])
        return expenses

    with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append({
                "id": int(row["id"]),
                "date": row["date"],
                "title": row["title"],
                "amount": float(row["amount"]),
                "category": row["category"]
            })
            
    return expenses


def save_all_expenses(expenses):
    """
    Saves the entire list of expenses back to the CSV file.
    """
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "date", "title", "amount", "category"])
        for exp in expenses:
            writer.writerow([exp["id"], exp["date"], exp["title"], exp["amount"], exp["category"]])


def get_next_id(expenses):
    """
    Finds the next unique ID for a new expense.
    """
    if not expenses:
        return 1
    return max(exp["id"] for exp in expenses) + 1


def display_table(expenses_list, header_title="EXPENSES"):
    """
    Helper function: Formats and displays any list of expenses in a clean table.
    Avoids writing print loops again and again (DRY Principle).
    """
    print("\n" + "=" * 65)
    print(f"               📋 {header_title}")
    print("=" * 65)
    
    if not expenses_list:
        print("No expenses found matching the criteria.")
        return

    print(f"{'ID':<5} | {'Date':<12} | {'Title':<20} | {'Category':<12} | {'Amount (₹)':>10}")
    print("-" * 65)

    subtotal = 0.0
    for exp in expenses_list:
        print(f"{exp['id']:<5} | {exp['date']:<12} | {exp['title']:<20} | {exp['category']:<12} | {exp['amount']:>10.2f}")
        subtotal += exp["amount"]

    print("-" * 65)
    print(f"{'TOTAL:':<53} ₹{subtotal:>10.2f}")


def add_expense():
    """
    Feature 1: Add a new expense.
    """
    print("\n" + "=" * 40)
    print("           ➕ ADD NEW EXPENSE")
    print("=" * 40)
    
    expenses = load_expenses()

    # 1. Title validation
    title = input("Enter expense title (e.g. Lunch, Metro recharge): ").strip()
    if not title:
        print("❌ Error: Title cannot be empty!")
        return

    # 2. Amount validation
    try:
        amount_input = input("Enter amount spent (in ₹): ").strip()
        amount = float(amount_input)
        if amount <= 0:
            print("❌ Error: Amount must be greater than 0.")
            return
    except ValueError:
        print("❌ Error: Please enter a valid numerical amount.")
        return

    # 3. Category selection
    print("\nSelect a Category:")
    for index, cat in enumerate(CATEGORIES, start=1):
        print(f"  {index}. {cat}")
    
    try:
        cat_choice = int(input(f"Choose category (1-{len(CATEGORIES)}): ").strip())
        if 1 <= cat_choice <= len(CATEGORIES):
            category = CATEGORIES[cat_choice - 1]
        else:
            category = "Others"
            print("⚠️ Invalid choice. Set to 'Others'.")
    except ValueError:
        category = "Others"
        print("⚠️ Invalid choice. Set to 'Others'.")

    # 4. Date validation
    today_str = datetime.now().strftime("%Y-%m-%d")
    date_input = input(f"Enter date (YYYY-MM-DD) [Press Enter for Today: {today_str}]: ").strip()
    
    if not date_input:
        date = today_str
    else:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            date = date_input
        except ValueError:
            print("❌ Error: Invalid date format! Please use YYYY-MM-DD.")
            return

    new_expense = {
        "id": get_next_id(expenses),
        "date": date,
        "title": title,
        "amount": amount,
        "category": category
    }

    expenses.append(new_expense)
    save_all_expenses(expenses)

    print(f"\n✅ Expense added successfully! (ID: {new_expense['id']})")


def view_all_expenses():
    """
    Feature 2: View all expenses.
    """
    expenses = load_expenses()
    display_table(expenses, "ALL RECORDED EXPENSES")


def search_and_filter():
    """
    Feature 3: Search expenses by Title, Category, or Date.
    """
    expenses = load_expenses()
    if not expenses:
        print("\n⚠️ No expenses found to search.")
        return

    print("\n" + "=" * 40)
    print("       🔍 SEARCH & FILTER EXPENSES")
    print("=" * 40)
    print(" 1. Search by Title (Keyword)")
    print(" 2. Filter by Category")
    print(" 3. Filter by Specific Date")
    print(" 0. Go Back")
    
    choice = input("Enter choice (0-3): ").strip()
    
    if choice == "1":
        keyword = input("Enter search word (e.g. 'Coffee', 'Book'): ").strip().lower()
        # Case-insensitive title search
        results = [e for e in expenses if keyword in e["title"].lower()]
        display_table(results, f"SEARCH RESULTS FOR: '{keyword}'")

    elif choice == "2":
        print("\nSelect Category to filter:")
        for index, cat in enumerate(CATEGORIES, start=1):
            print(f"  {index}. {cat}")
        try:
            cat_choice = int(input(f"Choose (1-{len(CATEGORIES)}): ").strip())
            if 1 <= cat_choice <= len(CATEGORIES):
                selected_cat = CATEGORIES[cat_choice - 1]
                results = [e for e in expenses if e["category"].lower() == selected_cat.lower()]
                display_table(results, f"CATEGORY: {selected_cat}")
            else:
                print("❌ Invalid category number.")
        except ValueError:
            print("❌ Please enter a valid number.")

    elif choice == "3":
        date_query = input("Enter date to filter (YYYY-MM-DD): ").strip()
        results = [e for e in expenses if e["date"] == date_query]
        display_table(results, f"EXPENSES ON: {date_query}")

    elif choice == "0":
        return
    else:
        print("❌ Invalid search option.")


def monthly_summary():
    """
    Feature 4: Monthly Expense Summary & Category Breakdown.
    """
    expenses = load_expenses()
    if not expenses:
        print("\n⚠️ No expenses recorded yet.")
        return

    current_month_str = datetime.now().strftime("%Y-%m")
    print("\n" + "=" * 45)
    print("          📊 MONTHLY EXPENSE SUMMARY")
    print("=" * 45)
    month_input = input(f"Enter Month (YYYY-MM) [Press Enter for Current: {current_month_str}]: ").strip()
    
    if not month_input:
        month_input = current_month_str

    # Validate YYYY-MM
    try:
        datetime.strptime(month_input, "%Y-%m")
    except ValueError:
        print("❌ Error: Invalid format! Use YYYY-MM (e.g., 2026-10).")
        return

    # Filter expenses for that month
    month_expenses = [e for e in expenses if e["date"].startswith(month_input)]

    if not month_expenses:
        print(f"\n⚠️ No expenses found for month: {month_input}")
        return

    # Category-wise grouping using a dictionary
    category_totals = {cat: 0.0 for cat in CATEGORIES}
    total_spent = 0.0

    for exp in month_expenses:
        cat = exp["category"]
        if cat in category_totals:
            category_totals[cat] += exp["amount"]
        else:
            category_totals["Others"] += exp["amount"]
        total_spent += exp["amount"]

    # Display monthly summary report
    print("\n" + "-" * 50)
    print(f" Summary for: {month_input} (Total Transactions: {len(month_expenses)})")
    print("-" * 50)
    print(f"{'Category':<15} | {'Amount Spent (₹)':>18} | {'% of Total':>10}")
    print("-" * 50)

    for cat, amt in category_totals.items():
        if amt > 0:  # Only show categories that have spending
            pct = (amt / total_spent) * 100
            print(f"{cat:<15} | ₹{amt:>17.2f} | {pct:>9.1f}%")

    print("-" * 50)
    print(f"{'GRAND TOTAL':<15} | ₹{total_spent:>17.2f} | {'100.0%':>10}")
    print("-" * 50)


def delete_expense():
    """
    Feature 5: Delete an expense by unique ID.
    """
    expenses = load_expenses()
    if not expenses:
        print("\n⚠️ No expenses to delete.")
        return

    print("\n" + "=" * 40)
    print("           🗑️ DELETE AN EXPENSE")
    print("=" * 40)
    
    try:
        del_id = int(input("Enter Expense ID to delete: ").strip())
    except ValueError:
        print("❌ Error: ID must be a valid number.")
        return

    # Find the expense
    expense_to_delete = None
    for exp in expenses:
        if exp["id"] == del_id:
            expense_to_delete = exp
            break

    if not expense_to_delete:
        print(f"❌ Error: No expense found with ID {del_id}!")
        return

    # Show details and confirm
    print(f"\nFound Expense: ID {del_id} - '{expense_to_delete['title']}' of ₹{expense_to_delete['amount']} ({expense_to_delete['category']}) on {expense_to_delete['date']}")
    confirm = input("Are you sure you want to delete this? (y/n): ").strip().lower()

    if confirm == "y":
        # Keep all expenses except the one with del_id
        expenses = [exp for exp in expenses if exp["id"] != del_id]
        save_all_expenses(expenses)
        print(f"✅ Expense with ID {del_id} has been deleted successfully!")
    else:
        print("❌ Deletion cancelled.")


def main_menu():
    """
    Main loop showing the interactive menu to the user.
    """
    while True:
        print("\n" + "=" * 45)
        print("       💰 PERSONAL EXPENSE TRACKER 💰")
        print("=" * 45)
        print(" 1. Add Expense")
        print(" 2. View All Expenses")
        print(" 3. Search & Filter Expenses")
        print(" 4. Monthly Summary & Category Report")
        print(" 5. Delete an Expense")
        print(" 0. Exit")
        print("=" * 45)

        choice = input("Enter your choice (0-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            search_and_filter()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            delete_expense()
        elif choice == "0":
            print("\n👋 Thank you for using Personal Expense Tracker. Have a great day!")
            break
        else:
            print("❌ Invalid option! Please enter a number between 0 and 5.")


if __name__ == "__main__":
    main_menu()
