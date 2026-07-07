"""
Project 2: Expense Tracker
DecodeLabs - Python Programming Industrial Training Kit

Goal: Continuously accept expense amounts from the user, validate
the input, accumulate a running total, and display the final total
when the user chooses to stop.
"""


def expense_tracker():
    total = 0  # Accumulator - initialized OUTSIDE the loop (state must persist)

    print("=== Expense Tracker ===")
    print("Enter an expense amount, or type 'quit' to stop.\n")

    while True:
        user_input = input("Enter expense: ").strip()

        # Sentinel value check - graceful shutdown
        if user_input.lower() == "quit":
            break

        # Defensive coding - guard against invalid (non-numeric) input
        try:
            expense = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number (or 'quit').\n")
            continue

        if expense < 0:
            print("Expense can't be negative. Try again.\n")
            continue

        total += expense  # Accumulator pattern: total = total + new_expense
        print(f"Added {expense:.2f}. Running total: {total:.2f}\n")

    print(f"\nFINAL TOTAL: ${total:.2f}")


if __name__ == "__main__":
    expense_tracker()
