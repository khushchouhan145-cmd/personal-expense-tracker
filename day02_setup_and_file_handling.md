# Day 2: File Handling, Formats (CSV & JSON) & Environment Setup

**Project:** Personal Expense Tracker  
**Internship Day:** Day 2  
**Author:** Khushi  
**Deliverable:** Working environment verification, repository setup, folder structure establishment, and file handling practice.

---

## 1. Environment & Tools Verification

| Tool / Technology | Status | Verification Command | Notes |
| :--- | :--- | :--- | :--- |
| **Python** | Verified (v3.14.x) | `python --version` | Standard library (`csv`, `json`, `os`, `datetime`) ready. |
| **VS Code** | Configured | Integrated Terminal & Explorer | Used for coding, debugging, and terminal operations. |
| **Git CLI** | Configured & Linked | `git status` | Connected to remote GitHub origin repository. |
| **GitHub Remote** | Active | `git remote -v` | `https://github.com/khushchouhan145-cmd/personal-expense-tracker.git` |

---

## 2. Established Project Structure

```text
personal-expense-tracker/
│
├── day01_python_basics.py             # Day 1: Python fundamentals & expense data practice
├── day01_requirements_and_plan.md     # Day 1: Requirements review & input/output design
├── day02_file_handling_practice.py    # Day 2: File I/O, CSV, JSON, and Exception Handling
├── day02_setup_and_file_handling.md   # Day 2: Environment setup & file concepts notes
├── main.py                            # Core application logic & menu loop
├── expenses.csv                       # Primary persistent database
├── PROJECT_REPORT.md                  # Comprehensive internship project report
└── README.md                          # Repository documentation for GitHub
```

---

## 3. File Handling Concepts & Mechanisms

### A. Context Manager (`with open(...)`)
In Python, using `with open(...) as file:` ensures that the file stream is automatically closed as soon as the block terminates, even if an unexpected exception occurs. This eliminates memory leaks and file corruption risks.

### B. File Opening Modes
- `"r"`: Read mode (raises `FileNotFoundError` if file doesn't exist).
- `"w"`: Write mode (creates a new file or overwrites existing content).
- `"a"`: Append mode (adds new rows to the end of the file without deleting existing data).

---

## 4. Comparative Analysis: CSV vs. JSON for Expense Tracker

| Feature | CSV (Comma-Separated Values) | JSON (JavaScript Object Notation) |
| :--- | :--- | :--- |
| **Format** | Plain text table with comma delimiters | Key-value structured objects & arrays |
| **File Size** | Very compact; minimal overhead | Slightly larger due to repeating keys |
| **Spreadsheet Compatibility** | Direct open in Microsoft Excel & Google Sheets | Requires conversion or specialized viewers |
| **Why chosen for our project?** | **Selected:** Ideal for uniform tabular financial records with fixed columns (`id,date,title,amount,category`). | Ideal for nested or hierarchical data, but overkill for simple tabular expense rows. |

---

## 5. Exception Handling in File Operations
Whenever dealing with the filesystem, defensive programming is mandatory. Common exceptions handled in our implementation:
- `FileNotFoundError`: Gracefully caught when an expense file is missing; triggers auto-creation of a fresh file with proper header columns.
- `PermissionError`: Handled if file access rights are restricted by the OS.
- `ValueError`: Handled when parsing numerical amount strings from file rows.

---

## 6. Day 2 Deliverables Status
- [x] Python & VS Code environment verified.
- [x] GitHub repository established and synced.
- [x] Folder structure documented.
- [x] File reading/writing practice completed in `day02_file_handling_practice.py`.
- [x] CSV & JSON comparison and file exception handling documented.
