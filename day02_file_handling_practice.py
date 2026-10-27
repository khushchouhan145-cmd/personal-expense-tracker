"""
=============================================================================
Day 2: File Handling, CSV & JSON Basics, and Exception Handling
Author: Khushi
Topics Covered:
  1. Basic File I/O (Writing and Reading text files with Context Manager)
  2. CSV File Handling (csv.writer, csv.DictReader)
  3. JSON Basics (json.dump, json.load for expense records)
  4. Exception Handling for File Operations (FileNotFoundError, IOError)
=============================================================================
"""

import os
import csv
import json

print("=== DAY 2: FILE HANDLING & FORMATS PRACTICE ===\n")

# ---------------------------------------------------------------------------
# 1. Basic Text File Writing & Reading (Using Context Manager 'with open')
# ---------------------------------------------------------------------------
print("--- 1. Basic Text File Handling ---")
sample_notes_file = "day02_sample_note.txt"

# Writing to a text file
with open(sample_notes_file, mode="w", encoding="utf-8") as file:
    file.write("Day 2 Notes: Setting up Personal Expense Tracker project.\n")
    file.write("Learning persistent storage using Python standard library.\n")

print(f"[SUCCESS] Wrote notes to {sample_notes_file}")

# Reading from the text file
with open(sample_notes_file, mode="r", encoding="utf-8") as file:
    content = file.read()
    print("File Content:")
    print(content.strip())
print()


# ---------------------------------------------------------------------------
# 2. CSV File Handling (Core of our Project)
# ---------------------------------------------------------------------------
print("--- 2. CSV File Handling (Writing & Reading Expenses) ---")
sample_csv_file = "day02_sample_expenses.csv"

sample_data = [
    {"id": 1, "date": "2026-10-21", "title": "Coffee", "amount": 40.0, "category": "Food"},
    {"id": 2, "date": "2026-10-21", "title": "Notebook", "amount": 90.0, "category": "Education"},
    {"id": 3, "date": "2026-10-22", "title": "Bus Fare", "amount": 30.0, "category": "Travel"}
]

# Writing to CSV using csv.writer
with open(sample_csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write header row
    writer.writerow(["id", "date", "title", "amount", "category"])
    # Write data rows
    for item in sample_data:
        writer.writerow([item["id"], item["date"], item["title"], item["amount"], item["category"]])

print(f"[SUCCESS] Successfully created CSV file: {sample_csv_file}")

# Reading from CSV using csv.DictReader
print("\nReading data back from CSV:")
with open(sample_csv_file, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"  Expense #{row['id']}: {row['title']} - Rs. {float(row['amount']):.2f} ({row['category']}) on {row['date']}")
print()


# ---------------------------------------------------------------------------
# 3. JSON Basics (Alternative Data Serialization)
# ---------------------------------------------------------------------------
print("--- 3. JSON Basics (Serialization & Deserialization) ---")
sample_json_file = "day02_sample_expenses.json"

# Writing Python dictionaries to JSON using json.dump
with open(sample_json_file, mode="w", encoding="utf-8") as file:
    json.dump(sample_data, file, indent=4)

print(f"[SUCCESS] Exported expenses to JSON file: {sample_json_file}")

# Reading data back from JSON using json.load
with open(sample_json_file, mode="r", encoding="utf-8") as file:
    loaded_json = json.load(file)
    print(f"Successfully read {len(loaded_json)} records from JSON file.")
    print(f"First record title: '{loaded_json[0]['title']}', Amount: Rs. {loaded_json[0]['amount']}")
print()


# ---------------------------------------------------------------------------
# 4. Exception Handling in File Operations
# ---------------------------------------------------------------------------
print("--- 4. Exception Handling (Defensive File Reading) ---")

non_existent_file = "non_existent_records.csv"

try:
    print(f"Attempting to read non-existent file: {non_existent_file}")
    with open(non_existent_file, mode="r", encoding="utf-8") as file:
        data = file.read()
except FileNotFoundError:
    print(f"[CAUGHT ERROR] File '{non_existent_file}' was not found! Handled gracefully.")
except PermissionError:
    print(f"[CAUGHT ERROR] Permission denied while accessing '{non_existent_file}'.")
except Exception as e:
    print(f"[CAUGHT UNEXPECTED ERROR] {e}")

print("\n=== DAY 2 FILE HANDLING PRACTICE COMPLETED! ===")
