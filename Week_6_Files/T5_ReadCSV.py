import csv #Import standard CSV library
#Read CSV file and print headings in row valus
def read(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file) #Creats a CSV reader object

        #First row assumed to be headings
        headings = next(csv_reader)
        print(f"Headings:\n {headings}")

        print("Values:")
        #Remaining Rows are data recods
        for values in csv_reader:
            print(values)

#Entry function for CS-reading task
def run_task1():
    read("clothing.csv")

if __name__ == "__main__":
    run_task1()