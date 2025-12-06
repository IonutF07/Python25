print ("Program started!")
ch = input("Please enter a standard character:\n").strip()
#Validate that exactly one character was entered
if len(ch) == 1:
    ascii_code = ord(ch) # convert character to ASCII
    print(f"The ASCII code for {ch} is {ascii_code}")
print("Program ended")