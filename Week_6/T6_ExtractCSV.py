import csv
#Extract and display item names (2nd column) from CSV file
def extract(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        next(csv_reader) #Skip the head row

        names = ""      #Accumulate the item names, one per line
        for values in csv_reader:
            #values [1] refers to the second column in each CSV row
            names += f"{values[1]}\n"
    print("Done!")
    print(f"The extracted items are:\n{names}")

#Entry function for this extraction task
def run_task2():
    extract("clothing.csv")

if __name__ == '__main__':
    run_task2()
