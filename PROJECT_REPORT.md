# INTERNSHIP PROJECT REPORT
## Title: Personal Expense Tracker Application
**Technology:** Python 3, VS Code, CSV File Handling  
**Domain:** Python Programming & Software Development  
**Submission Type:** Mini Project / Internship Assignment  

---

### 1. ABSTRACT
The Personal Expense Tracker is a console-based software application built using core Python. The application enables users to manage their daily financial expenditures systematically. It addresses common financial tracking difficulties by offering functionalities like recording expenses with specific categories and dates, displaying all historical records, keyword searching, category filtering, monthly spending aggregation, and record deletion. All transaction data is stored persistently using Comma-Separated Values (CSV) file storage.

---

### 2. OBJECTIVES OF THE PROJECT
1. To design a user-friendly, menu-driven CLI interface.
2. To implement CRUD operations (Create, Read, Update/Search, Delete) on expense records.
3. To enforce categorization across predefined financial categories (Food, Travel, Shopping, Education, Bills, Healthcare, Others).
4. To implement persistent data storage without relying on heavy external database software.
5. To provide analytical summaries including monthly totals and percentage breakdowns.
6. To implement input validation and error handling to prevent application crashes.

---

### 3. SYSTEM ARCHITECTURE & DATA FLOW

```text
[User Input via Console]
         │
         ▼
[Input Validation Layer] ── (Checks Amount > 0, Date Format YYYY-MM-DD)
         │
         ▼
[Core Business Logic] ──── (Add, View, Search, Delete, Monthly Summary)
         │
         ▼
[Data Storage Layer] ───── (Reads / Writes to expenses.csv using Python csv module)
```

---

### 4. MODULES DESCRIPTION

| Module / Function | Purpose |
| :--- | :--- |
| `load_expenses()` | Reads records from `expenses.csv` into a memory list of dictionaries. Auto-creates headers if file is absent. |
| `save_all_expenses()` | Writes all current memory records back to `expenses.csv`. |
| `add_expense()` | Prompts user for title, amount, category, and date with real-time validation. |
| `view_all_expenses()` | Displays formatted table of all expenses along with running total. |
| `search_and_filter()` | Allows multi-parameter query (by Title keyword, Category, or exact Date). |
| `monthly_summary()` | Aggregates expenses for a user-specified month (`YYYY-MM`) and calculates percentage per category. |
| `delete_expense()` | Locates an expense by ID, requests user confirmation, and removes it safely. |
| `main_menu()` | Infinite execution loop (`while True`) providing user navigation. |

---

### 5. PYTHON CONCEPTS APPLIED
1. **Data Structures:**
   - `Dictionary`: Used to model an individual expense item with key-value pairs (`id`, `title`, `amount`, `category`, `date`).
   - `List`: Used to store the active collection of all expense dictionaries.
2. **File Handling:**
   - Standard library `csv` module with `csv.DictReader` and `csv.writer`.
3. **Defensive Programming & Exception Handling:**
   - Handled `ValueError` during integer/float conversions and date string parsing.
4. **Modularity & Reusability:**
   - Followed DRY (Don't Repeat Yourself) principle by creating a reusable table formatter (`display_table()`).

---

### 6. TESTING & VALIDATION

| Test Case | Input | Expected Output | Status |
| :--- | :--- | :--- | :--- |
| Add Valid Expense | Title: "Lunch", Amount: 150, Cat: Food | Record created with new unique ID | Passed |
| Non-numeric Amount | Amount: "abc" | Error prompt: "Please enter a valid numerical amount" | Passed |
| Invalid Date Format | Date: "21-10-2026" | Error prompt: "Invalid date format! Use YYYY-MM-DD" | Passed |
| Search by Keyword | Keyword: "lunch" | Displays matching records case-insensitively | Passed |
| Delete with Confirmation | Confirm: 'n' | Record preserved; message: "Deletion cancelled" | Passed |

---

### 7. CONCLUSION & FUTURE SCOPE
The project successfully achieves all requirements set out for the internship mini-project. It offers an efficient, dependency-free solution for personal finance management.
- **Future Enhancements:**
  1. Adding data visualization charts (using `matplotlib`).
  2. Exporting monthly reports to PDF format.
  3. Developing a graphical user interface (GUI) using Tkinter or web interface using Flask.
