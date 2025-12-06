def pattern():
    # Return a dictionary containing three pattern lengths and their counts.
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences

def display_keys(data):
    #Print all keys in the dictionary.
    print("Keys:")
    for key in data.keys():
        print(key)

def display_values(data):
    # Print all values in the dictionary.
    print("Values:")
    for value in data.values():
        print(value)

def display_items(data):
    # Print all key–value pairs in the dictionary.
    print("Pairs:")
    for key, value in data.items():
        print(f"{key}: {value}")

def run():
    # Display the dictionary, its keys, its values and its key–value pairs.
    sequences = pattern()
    print(f"Dictionary:\n{sequences}\n")
    display_keys(sequences)
    print()
    display_values(sequences)
    print()
    display_items(sequences)

if __name__ == "__main__":
    run()