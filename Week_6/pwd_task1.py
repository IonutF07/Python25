import os  #Standard library module for working with the file system

#Display the current working directory and list of file in it
def cwd():
    path = os.getcwd() #Get absolute oath of the current working directory
    print(f"Current working directory is: {path}")
    print(f"The directory contains the following:")
    for file in os.listdir(path): #Loop through all entries in the directory
        print(file)

#Simple entry function to run the task
def run():
    print("Processing...")
    cwd()

#Standard Python entry point guard
if __name__ == "__main__":
    run()