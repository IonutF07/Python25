#Read a file line-by-line and display each location searched
def search(file_path):
    print("Searching...")

#Open a file and iterate directly over its line
    with open(file_path) as file:
        for location in file:
            #strip() removes the newline character at the end of each
            print(f"Looked in {location.strip()}")
    print("Done!")
#Entry function for this activity
def run_task3():
    search("library.txt")
if __name__ == "__main__":
    run_task3()