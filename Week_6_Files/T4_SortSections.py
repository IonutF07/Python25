#Read a text file and separate lines into sections and books
def search(file_path):
    print("Searching...")
    sections = "" #Will Store all section lines
    books = "Books:\n" #Heading for the list of books

    with open(file_path) as file:
        for line in file:
        #Sections are identified by the line starting with the word 'Section'
            if line.startswith("Section"):
                sections += line
            else:
                books += line
    print("Done!")
    #Combine sections and books with a blank line between them
    return f"{sections}\n{books}"

#Save given text data to a file
def save(file_path, data):
    print("Saving...")
    #Open in write mode to overwrite any existing content
    with open(file_path,"w") as file:
        file.write(data)
    print("Done!")

#Overall runner for this activity
def run():
    data = search("books.txt")              #Process the source file
    save("exported_books.txt", data)  #Save result to a new file

if __name__ == "__main__":
    run()