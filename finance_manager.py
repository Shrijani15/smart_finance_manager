import pandas as pd
import os

FILE_NAME = "finance_data.csv"


# Initialize file
def init_file():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["Type", "Category", "Amount"])
        df.to_csv(FILE_NAME, index=False)


# Add transaction
def add_transaction():
    print("\n--- Add Transaction ---")

    t_type = input("Enter Type (Income/Expense): ").capitalize()
    if t_type not in ["Income", "Expense"]:
        print("Invalid type!")
        return

    category = input("Enter Category: ")

    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    df = pd.read_csv(FILE_NAME)

    new_data = pd.DataFrame([[t_type, category, amount]],
                            columns=["Type", "Category", "Amount"])

    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

    print("Transaction added successfully!")


# View summary
def view_summary():
    print("\n--- Financial Summary ---")

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No data available!")
        return

    income = df[df["Type"] == "Income"]["Amount"].sum()
    expense = df[df["Type"] == "Expense"]["Amount"].sum()

    print(f"Total Income  : ₹{income}")
    print(f"Total Expense : ₹{expense}")
    print(f"Balance       : ₹{income - expense}")


# Smart suggestion
def smart_suggestion():
    print("\n--- Smart Insight ---")

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No data available!")
        return

    income = df[df["Type"] == "Income"]["Amount"].sum()
    expense = df[df["Type"] == "Expense"]["Amount"].sum()

    if expense > income:
        print("Warning: You are overspending!")
    elif expense > 0.8 * income:
        print("Caution: Expenses are high!")
    else:
        print(" Good job! Your spending is under control.")


# Menu
def menu():
    init_file()

    while True:
        print("\n====== SMART FINANCE MANAGER ======")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. Smart Suggestion")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            smart_suggestion()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")
# Run
if __name__ == "__main__":
    menu()