# 💰 Personal Expense Tracker (Python Mini Project)

A clean, menu-driven Python console application developed as part of an **internship project** to record, manage, search, and analyze daily expenses. Data is stored permanently in a structured CSV file.

---

## 📌 Project Overview

Managing personal finances is essential for financial discipline. The **Personal Expense Tracker** provides a lightweight, easy-to-use command-line interface (CLI) to track daily spending, categorize expenses, search through transaction history, and generate monthly financial summaries with category-wise percentage breakdowns.

---

## 🚀 Key Features

1. **Add Expense**:
   - Record expense details: Title, Amount, Category, and Date.
   - Automatically assigns a unique incremental ID to every transaction.
   - Defaults to today's date if no custom date is specified.

2. **Predefined Expense Categories**:
   - `Food`, `Travel`, `Shopping`, `Education`, `Bills`, `Healthcare`, and `Others`.

3. **View All Expenses**:
   - Displays all records in a formatted tabular layout with aligned columns and a running grand total.

4. **Search and Filter Expenses**:
   - Search by keyword in Title (case-insensitive partial matching).
   - Filter records by specific Category.
   - Filter records by specific Date (`YYYY-MM-DD`).

5. **Monthly Expense Summary & Analytics**:
   - Summarizes total expenses for any selected month (`YYYY-MM`).
   - Generates a category-wise spending report with percentages (`% of Total`).

6. **Delete Expense**:
   - Delete any incorrect entry safely using its unique ID with a confirmation prompt (`y/n`).

7. **Persistent CSV Storage**:
   - All transactions are stored permanently in `expenses.csv`.
   - Data persists across application restarts.

8. **Robust Input Validation & Error Handling**:
   - Protects against invalid numbers, non-existent categories, empty titles, and incorrect date formats using `try...except` blocks.

---

## 🛠️ Technology Stack

- **Programming Language**: Python 3.x
- **Development Environment**: Visual Studio Code (VS Code)
- **Data Storage**: CSV (Comma-Separated Values) via Python's built-in `csv` module
- **Libraries Used**: Standard Python Libraries only (`csv`, `os`, `datetime`) — *No external `pip` dependencies required!*

---

## 📁 Project Structure

```text
personal-expense-tracker/
│
├── expenses.csv       # Persistent database storing all expense records
├── main.py            # Complete application source code (menu, logic, validation)
└── README.md          # Comprehensive project documentation
```

---

## ⚙️ How to Run the Project in VS Code

### Prerequisites:
- Python 3.x installed on your system.
- Visual Studio Code installed.

### Step-by-Step Execution:
1. **Open the Project**:
   - Launch VS Code.
   - Go to `File` > `Open Folder...` and select the `personal-expense-tracker` folder.

2. **Open Terminal in VS Code**:
   - Press ``Ctrl + ` `` (Backtick) or go to `Terminal` > `New Terminal`.

3. **Run the Script**:
   ```bash
   python main.py
   ```

---

## 🖥️ Sample Application Menu & Walkthrough

```text
=============================================
       💰 PERSONAL EXPENSE TRACKER 💰
=============================================
 1. Add Expense
 2. View All Expenses
 3. Search & Filter Expenses
 4. Monthly Summary & Category Report
 5. Delete an Expense
 0. Exit
=============================================
Enter your choice (0-5):
```

### Sample Output: View All Expenses
```text
=================================================================
               📋 ALL RECORDED EXPENSES
=================================================================
ID    | Date         | Title                | Category     | Amount (₹)
-----------------------------------------------------------------
1     | 2026-10-20   | Lunch                | Food         |     150.00
2     | 2026-10-21   | Metro Card Recharge  | Travel       |     300.00
3     | 2026-10-21   | Python Course Book   | Education    |     450.00
-----------------------------------------------------------------
TOTAL:                                                ₹    900.00
```

### Sample Output: Monthly Summary Report
```text
--------------------------------------------------
 Summary for: 2026-10 (Total Transactions: 3)
--------------------------------------------------
Category        |   Amount Spent (₹) | % of Total
--------------------------------------------------
Food            | ₹           150.00 |      16.7%
Travel          | ₹           300.00 |      33.3%
Education       | ₹           450.00 |      50.0%
--------------------------------------------------
GRAND TOTAL     | ₹           900.00 |     100.0%
--------------------------------------------------
```

---

## 🧠 Python Concepts Applied (Internship Learning)

- **Data Structures**: Lists (`[]`) for ordered records and Dictionaries (`{}`) for key-value transaction properties.
- **File Handling**: Reading and writing `.csv` files using `csv.DictReader` and `csv.writer`.
- **Control Flow**: `while` loops for continuous menu navigation and `if-elif-else` conditional branching.
- **String Formatting**: Aligned string formatting (`f"{text:<20}"`) to build terminal tables without external tabular libraries.
- **Exception Handling**: Safeguarding user inputs using `try...except ValueError` blocks.
- **Date Manipulation**: Working with real-time timestamps using `datetime.now()` and string parsing via `strptime`.

---

## 📤 Submission & GitHub Commands

To submit this project to GitHub:

```bash
# 1. Initialize git repository
git init

# 2. Add all project files
git add .

# 3. Create initial commit
git commit -m "feat: complete personal expense tracker project"

# 4. Link to your remote GitHub repository
git remote add origin https://github.com/<your-username>/personal-expense-tracker.git

# 5. Push to GitHub
git branch -M main
git push -u origin main
```
