rows = int(input("\n Enter the number of rows:\n "))
print()
cols = int(input("\n Enter the number of columns:\n "))
print("\n Here I go:\n")
for r in range(rows):
        for c in range(cols):
            print(":-)", end=" ")
        print()  # Move to the next line after each row
print("\nAll done!")