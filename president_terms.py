"""First Ten U.S. Presidents.

This program displays the first ten U.S. presidents and their terms with both a for
loop and a while loop. It also validates user input and demonstrates string searching.

The program uses lists, loops, conditions, text operations, and `try`/`except` handling
to keep the interaction understandable when input is not valid.
"""


# Each tuple keeps a president's name paired with the term shown beside it.
PRESIDENTS = [
    ("George Washington", "1789-1797"),
    ("John Adams", "1797-1801"),
    ("Thomas Jefferson", "1801-1809"),
    ("James Madison", "1809-1817"),
    ("James Monroe", "1817-1825"),
    ("John Quincy Adams", "1825-1829"),
    ("Andrew Jackson", "1829-1837"),
    ("Martin Van Buren", "1837-1841"),
    ("William Henry Harrison", "1841"),
    ("John Tyler", "1841-1845"),
]


def get_president_count():
    """Ask how many entries to display and recover from invalid numeric input."""
    # Keep prompting until the user gives a whole number that fits the size of the list.
    while True:
        try:
            # int() converts the typed count so it can be used with list slicing.
            count = int(input("How many presidents would you like to display (1-10)? ").strip())
            if 1 <= count <= len(PRESIDENTS):
                return count
            print("Please enter a whole number from 1 through 10.")
        except ValueError:
            # A non-integer would fail conversion, so this gives a clear retry message.
            print("Please enter a whole number from 1 through 10.")


def get_search_term():
    """Get a short search term after removing extra spaces around it."""
    # strip() cleans whitespace, and len() keeps the search term at a reasonable size.
    while True:
        term = input("Enter a president name or word to search for (1-30 characters): ").strip()
        if 1 <= len(term) <= 30:
            return term
        print("Please enter a search term between 1 and 30 characters.")


def format_president(name, term):
    """Add an asterisk when the president's last name begins with A."""
    # split() separates the name so the last word can be checked by the if/else condition.
    last_name = name.split()[-1]
    if last_name.startswith("A"):
        return f"* {name}: {term}"
    return f"  {name}: {term}"


def main():
    """Display president data with both required loop types and report search results."""
    count = get_president_count()
    search_term = get_search_term()
    selected_presidents = PRESIDENTS[:count]

    # Print each selected president and term with a for loop.
    print("\nFor loop output:")
    for name, term in selected_presidents:
        print(format_president(name, term))

    # Print the same selected presidents again with a while loop.
    print("\nWhile loop output:")
    index = 0
    while index < len(selected_presidents):
        name, term = selected_presidents[index]
        print(format_president(name, term))
        index += 1

    # lower() normalizes the search text, slicing reverses it, and the list comprehension finds matches.
    normalized_search = search_term.lower()
    reversed_search = normalized_search[::-1]
    matches = [
        name for name, _ in selected_presidents if normalized_search in name.lower()
    ]

    print(f"\nSearch term in lowercase: {normalized_search}")
    print(f"Search term reversed: {reversed_search}")
    print(f"Matching president names: {len(matches)}")
    if matches:
        print(", ".join(matches))
    else:
        print("No displayed president names matched that search term.")


if __name__ == "__main__":
    main()
