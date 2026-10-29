# Python Fundamentals

This repository contains two small Python 3 programs that use clear prompts, validate input, and handle errors with `try`/`except`.

## Files

- `simple_interest_calculator.py`: calculates simple interest from a principal, annual rate, and number of years. It also formats, reverses, and counts words in a short description.
- `president_terms.py`: displays the first ten U.S. presidents with both `for` and `while` loops. It adds an asterisk when a president's last name starts with `A` and searches names using a user-provided term.

## Run the programs

Python 3 is all that is needed. From the repository folder, run either command:

```powershell
python simple_interest_calculator.py
python president_terms.py
```

## Input limits

- Financial values and time must be greater than zero.
- Descriptions must contain 1 to 60 characters.
- President searches must contain 1 to 30 characters.
- The president program displays between 1 and 10 entries because the list contains the first ten presidents.

## Testing notes

Each program was checked with successful input and invalid input.

- In `simple_interest_calculator.py`, `abc`, `0`, and negative values prompt the user again. An empty description is also rejected. Principal `1000`, rate `5`, and time `2` return `$100.00`.
- In `president_terms.py`, `eleven`, `0`, and `11` prompt the user again. A search for `Adams` finds John Adams and John Quincy Adams. Empty and no-match searches show the expected messages.
