
word = input("What word do you see?\n")

print ("Displaying index positions...\n")
for i in range (0, len(word), 1):
    print (f"Index position {i}:{word[i]}")
print ("\n...Done")