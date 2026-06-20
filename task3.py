import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Amount", "Category"])


def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Shopping/etc): ")

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount, category])

    print("Expense added successfully!")


def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\nAll Expenses:")
        for row in reader:
            print(f"Date: {row[0]}, Description: {row[1]}, Amount: ₹{row[2]}, Category: {row[3]}")


def search_by_category():
    category = input("Enter category to search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print(f"\nExpenses in '{category}' category:")
        found = False

        for row in reader:
            if row[3].lower() == category.lower():
                print(f"Date: {row[0]}, Description: {row[1]}, Amount: ₹{row[2]}")
                found = True

        if not found:
            print("No expenses found.")


def total_per_category():
    totals = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            category = row[3]
            amount = float(row[2])

            totals[category] = totals.get(category, 0) + amount

    print("\nTotal Spending Per Category:")
    for category, total in totals.items():
        print(f"{category}: ₹{total}")


def monthly_spending():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0].startswith(month):
                total += float(row[2])

    print(f"\nTotal Spending for {month}: ₹{total}")


def menu():
    while True:
        print("\n----- Expense Tracker -----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Total Per Category")
        print("5. Monthly Spending")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            total_per_category()
        elif choice == "5":
            monthly_spending()
        elif choice == "6":
            print("Program Ended")
            break
        else:
            print("Invalid Choice")


create_file()
menu()
