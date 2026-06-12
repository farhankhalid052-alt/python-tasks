import csv
import os

FILE_NAME = "expenses.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Amount"])

def add_expense():
    description = input("Enter expense description: ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([description, amount])

    print("Expense added successfully!")

def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\\nExpenses:")
        for row in reader:
            print(f"Description: {row[0]}, Amount: ₹{row[1]}")

def calculate_total():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[1])

    print(f"\\nTotal Expenses: ₹{total}")

def menu():
    while True:
        print("\\n----- Expense Tracker -----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Program Ended")
            break
        else:
            print("Invalid Choice")

create_file()
menu()
