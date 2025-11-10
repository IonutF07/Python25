#display initial message
print("What level of brightness is required?")

brighteness_level = int(input())
#use a for loop to display brightness levels
for level in range(1, brighteness_level + 1, 2):
    print("*" * level)