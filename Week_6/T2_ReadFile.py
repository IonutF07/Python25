#Read a specific number of characters from a text file
def display_char(file_path, num_chars):
#'with ensures the file is closed automatically
    with open (file_path) as file:
        data = file.read(num_chars) #Read the only given number of characters
    print(data)

#Read a single line from a text file
def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip() #Read one line and remove trailing newline
        print(data)

#Read the entire contents of a text file
def display_text(file_path):
    with open(file_path) as file:
        data = file.read() #Read the full file content as one string
        print(data)

#Run all three reading functions on library.txt
def run_task2():
    display_char("library.txt",5)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run_task2()