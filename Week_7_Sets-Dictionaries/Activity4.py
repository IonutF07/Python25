def pattern():
    # Create and return a dictionary that maps pattern names to their counts.
    sequences = {"Short Sequence": 3,"Medium Sequence": 2,"Long Sequence": 1}
    return sequences

def run():
    # Display the dictionary returned by pattern().
    sequences = pattern()
    print(sequences)

if __name__ == "__main__":
    run()