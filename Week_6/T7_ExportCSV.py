#Append a given numbers of items to a CSV file using user input
def export(file_path,num_items):
    print("Exporting...")
    #Open in append mode so we add to, rather than overwrite the file
    with open(file_path,"a") as file:
        for count in range(num_items):
            print("Please enter the item id:")
            item_id = int(input()) #Convert input string to integer

            print("Please enter the item name:")
            item_name = input()

            print("Please enter the item colour:")
            item_colour = input()

            #Build a simple CSV line: id,name,colour
            data = f"{item_id},{item_name},{item_colour}\n"
            file.write(data)
        print("Done!")

#Entry function to test the export with two items.
def run_task3():
    export("exported_items.csv",2)

if __name__ == "__main__":
    run_task3()