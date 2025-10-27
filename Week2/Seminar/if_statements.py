print ("What kind of book are you reading?")#
bookname = input()
if bookname.lower() == "adventure":
    print (f"I like {bookname} books!.")
    print ("\n Finished reading book.")


print ("Please enter the activity to be performed")#
activity = input()
if activity.lower() == "calculate":
    print ("Performing Calculations...:")
    print ("Activity completed!")
else:
    print ("You entered a wrong activity.")

