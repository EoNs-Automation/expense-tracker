def main():
    expenses = []
    categories = ["Food", "Transport", "Entertainment", "Bills", "Other"]

    print("=== Expense Tracker ===")
    print("Type 'quit' at any time to exit.\n")

    while True:
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Delete expense")
        print("5. Quit")

        choice = input("\nChoose an option (1-5): ").strip().lower()

        if choice == "5" or choice == "quit":
            print("Goodbye!")
            break

        elif choice == "1":
            description = input("Description: ").strip()
            if description.lower() == "quit":
                break

            amount_input = input("Amount: ").strip()
            if amount_input.lower() == "quit":
                break

            try:
                amount = float(amount_input)
            except ValueError:
                print("Please enter a valid number.\n")
                continue

            print("\nCategories:")
            for i, cat in enumerate(categories, 1):
                print(f"{i}. {cat}")

            cat_choice = input("Choose category (1-5): ").strip()
            if cat_choice.isdigit() and 1 <= int(cat_choice) <= 5:
                category = categories[int(cat_choice) - 1]
            else:
                category = "Other"

            expenses.append({
                "description": description,
                "amount": amount,
                "category": category
            })
            print("Expense added!\n")

        elif choice == "2":
            if not expenses:
                print("No expenses yet.\n")
            else:
                print("\n--- Expenses ---")
                for i, expense in enumerate(expenses, 1):
                    print(f"{i}. [{expense['category']}] {expense['description']}: ${expense['amount']:.2f}")
                print()

        elif choice == "3":
            if not expenses:
                print("No expenses yet.\n")
            else:
                total = sum(expense["amount"] for expense in expenses)
                print(f"\nTotal spent: ${total:.2f}\n")

                # Show totals by category
                print("By category:")
                for cat in categories:
                    cat_total = sum(e["amount"] for e in expenses if e["category"] == cat)
                    if cat_total > 0:
                        print(f"  {cat}: ${cat_total:.2f}")
                print()

        elif choice == "4":
            if not expenses:
                print("No expenses to delete.\n")
                continue

            print("\n--- Expenses ---")
            for i, expense in enumerate(expenses, 1):
                print(f"{i}. [{expense['category']}] {expense['description']}: ${expense['amount']:.2f}")

            delete_choice = input("\nEnter the number to delete: ").strip()
            if delete_choice.isdigit() and 1 <= int(delete_choice) <= len(expenses):
                removed = expenses.pop(int(delete_choice) - 1)
                print(f"Deleted: {removed['description']}\n")
            else:
                print("Invalid number.\n")

        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()