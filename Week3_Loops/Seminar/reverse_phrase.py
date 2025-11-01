word = input("What word do you want to see in reverse?\n")

print("\nReversing the word...\n")
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print(f"The reversed word is: {reversed_word}")