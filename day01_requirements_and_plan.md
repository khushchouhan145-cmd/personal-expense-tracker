# Day 1: Requirements Review & System Design Plan

**Project:** Personal Expense Tracker  
**Internship Day:** Day 1  
**Author:** Khushi  
**Deliverable:** Review project requirements, identify system inputs/outputs, and design the expense data representation.

---

## 1. Project Requirements Review

The goal of this project is to build an interactive, menu-driven Python application that allows users to record, manage, search, and analyze their daily expenses with persistent CSV storage.

### Core Objectives Identified:
1. Accept expense transactions from users with valid categories and dates.
2. Maintain persistent storage so records survive application restart.
3. Present clean, readable tabular reports without relying on heavy external GUI or database frameworks.
4. Provide search, category filtering, and monthly spending insights.
5. Provide safe deletion with user confirmation.

---

## 2. Identification of System Inputs & Outputs

| Feature | Input Parameters | System Validation Rules | Expected Output |
| :--- | :--- | :--- | :--- |
| **Add Expense** | - Title (text)<br>- Amount (number)<br>- Category (choice 1-7)<br>- Date (YYYY-MM-DD or Enter) | - Title cannot be empty.<br>- Amount must be a positive float (> 0).<br>- Category mapped to predefined list.<br>- Date must match `YYYY-MM-DD` format. | Success notification with newly assigned unique ID. Record appended to CSV. |
| **View All Expenses** | - Menu selection `2` | - Ensure data file exists and contains valid records. | Formatted console table displaying ID, Date, Title, Category, and Amount with a grand total sum. |
| **Search & Filter** | - Search Type (1: Title, 2: Category, 3: Date)<br>- Query string / choice | - Case-insensitive partial matching for Title.<br>- Valid category index for Category.<br>- Exact date format for Date. | Filtered subset table showing only matching transactions. |
| **Monthly Summary** | - Target month string (`YYYY-MM`) | - Validate `YYYY-MM` format. Default to current month if blank. | Aggregated summary table showing Category breakdown, total amount spent, and percentage of overall monthly spend. |
| **Delete Expense** | - Expense ID (integer)<br>- Confirmation (`y` / `n`) | - ID must exist in current record list.<br>- Deletion occurs only if user inputs `y`. | Confirmation message and updated record list saved back to CSV. |

---

## 3. Expense Data Representation Plan

### A. Single Expense Record Representation: `Dictionary`
Each individual expense is modeled as a Python dictionary (`dict`) with 5 defined keys:

```python
expense = {
    "id": 1,                     # int: Unique incremental identifier
    "date": "2026-10-21",        # str: ISO formatted date (YYYY-MM-DD)
    "title": "College Books",    # str: Descriptive title
    "amount": 450.50,            # float: Monetary value in INR
    "category": "Education"      # str: One of the 7 predefined categories
}
```

**Why a Dictionary?**
- Key-based access (`expense["amount"]`) is much less error-prone and more readable than index-based access (`expense[3]`).
- Directly maps to columns when converting to/from CSV rows.

### B. In-Memory Collection: `List of Dictionaries`
All records currently active in the program will be held in a Python list:
```python
expenses = [
    {"id": 1, "date": "2026-10-20", "title": "Lunch", "amount": 150.0, "category": "Food"},
    {"id": 2, "date": "2026-10-21", "title": "Metro Recharge", "amount": 300.0, "category": "Travel"}
]
```

**Why a List?**
- Preserves the chronological order of expenses.
- Supports iteration (`for exp in expenses:`), filtering via list comprehensions, and length counting (`len(expenses)`).

---

## 4. Day 1 Deliverable Status
- [x] Python fundamentals (variables, operators, conditionals, loops, functions, data structures) practiced in `day01_python_basics.py`.
- [x] Project requirements analyzed and inputs/outputs identified.
- [x] Data representation structure (Dictionary + List) finalized for the core implementation.
