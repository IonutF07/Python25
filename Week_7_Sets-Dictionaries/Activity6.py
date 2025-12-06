def short_pattern():
    # Return a dictionary describing the short pattern.
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern

def medium_pattern():
    # Return a dictionary describing the medium pattern.
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern

def long_pattern():
    # Return a dictionary describing the long pattern.
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern

def run_task3():
     # Create a dictionary of dictionaries and display all patterns.
    print("Analysing patterns...")
    patterns = {"short sequence": short_pattern(), "medium sequence": medium_pattern(),
        "long sequence": long_pattern()}

    for name, pattern in patterns.items():
        print(f"{name}: {pattern}")

if __name__ == "__main__":
    run_task3()