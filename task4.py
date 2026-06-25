import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"
HEADERS = ["id", "date", "description", "amount", "category"]


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)


def generate_id():
    return str(int(datetime.now().timestamp()))


def add_expense():
    description = input("Enter description: ").strip()
    category = input("Enter category: ").strip()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Amount must be numeric.")
        return

    if not category:
        print("Category cannot be empty.")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([generate_id(), date, description, amount, category])

    print("Expense added successfully.")


def read_expenses():
    with open(FILE_NAME, "r", newline="") as file:
        return list(csv.DictReader(file))


def view_all():
    rows = read_expenses()

    if not rows:
        print("No expenses found.")
        return

    total = 0
    print("\nID | Date | Description | Amount | Category")
    print("-" * 60)

    for row in rows:
        print(f"{row['id']} | {row['date']} | {row['description']} | ₹{row['amount']} | {row['category']}")
        total += float(row["amount"])

    print("-" * 60)
    print(f"Count: {len(rows)}")
    print(f"Total: ₹{total:.2f}")


def search_by_category():
    search = input("Enter category: ").strip().lower()
    rows = read_expenses()

    subtotal = 0
    found = False

    for row in rows:
        if row["category"].lower() == search:
            print(row)
            subtotal += float(row["amount"])
            found = True

    if found:
        print(f"Subtotal for {search}: ₹{subtotal:.2f}")
    else:
        print("No matching records found.")


def monthly_total():
    month = input("Enter month (YYYY-MM): ").strip()
    total = 0

    for row in read_expenses():
        if row["date"].startswith(month):
            total += float(row["amount"])

    print(f"Monthly Total for {month}: ₹{total:.2f}")


def delete_by_id():
    delete_id = input("Enter ID to delete: ").strip()
    rows = read_expenses()

    updated_rows = [row for row in rows if row["id"] != delete_id]

    if len(updated_rows) == len(rows):
        print("ID not found.")
        return

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(updated_rows)

    print("Expense deleted successfully.")


def run():
    create_file()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All")
        print("3. Search by Category")
        print("4. Monthly Total (YYYY-MM)")
        print("5. Delete by ID")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            monthly_total()
        elif choice == "5":
            delete_by_id()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    run()
