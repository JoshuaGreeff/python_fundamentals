"""Simple Interest Calculator.

This program asks for a principal amount, interest rate, time in years, and a short
description. It validates input, calculates simple interest, and demonstrates basic
string transformation and analysis.

The functions below show validated input, specific error recovery, and simple text
operations before displaying a result.
"""


def get_positive_number(prompt):
    """Keep asking until the user provides a positive number."""
    # A loop lets the program recover from bad input instead of stopping after one attempt.
    while True:
        try:
            # float() converts typed text into a number so it can be used in the formula.
            value = float(input(prompt).strip())
            # A principal, rate, or time of zero or less is not useful for this calculation.
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            # ValueError catches text such as "abc" and gives the user another chance.
            print("That was not a valid number. Please try again.")


def get_description():
    """Get a short label for the calculation and enforce a simple length limit."""
    # strip() removes accidental spaces at the beginning or end of the typed description.
    while True:
        description = input("What is this calculation for? (1-60 characters): ").strip()
        # len() keeps the description short enough to display cleanly.
        if 1 <= len(description) <= 60:
            return description
        print("Please enter a description between 1 and 60 characters.")


def main():
    """Collect values, calculate simple interest, and display the result."""
    print("Simple Interest Calculator")

    # Collect clean numeric values before using them in the interest formula.
    principal = get_positive_number("Enter the principal amount: $")
    rate = get_positive_number("Enter the annual interest rate (%): ")
    time = get_positive_number("Enter the time in years: ")
    description = get_description()

    # This applies the required formula: (Principal * Rate * Time) / 100.
    interest = (principal * rate * time) / 100

    # title() changes the display style, slicing reverses the text, and split() counts words.
    formatted_description = description.title()
    reversed_description = description[::-1]
    word_count = len(description.split())

    print(f"\nCalculation: {formatted_description}")
    print(f"Simple interest: ${interest:,.2f}")
    print(f"Words in the description: {word_count}")
    print(f"Description reversed: {reversed_description}")


if __name__ == "__main__":
    main()
