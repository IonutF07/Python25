#Cave exploration game using nested if statements for branching outcomes
print("You find a mysterious cave.")
print("Do you enter? (yes/no) ")
action = input().lower()

if action == "yes":
    print("You step inside the dark cave.")
    print("Do you have a torch? (yes/no) ")
    item = input().lower()
    if item == "yes":
        print("You light your torch and explore safely.")
        print("Do you see gold or jewels?.")
        treasure = input().lower()
        if treasure == "gold" or treasure == "jewels":
            print("You found treasure! You win!")
        else:
            print("Nothing valuable here, but you're safe.")
    else:
        print("You hear a noise. Is it loud? (yes/no)")
        sound = input().lower()
        if sound == "yes" and not item == "yes":
            print("It's too dangerous without light. You run out!")
        else:
            print("You carefully feel your way through.")

elif action == "no":
    print("You walk away safely. Game over.")
else:
    print("Invalid choice. The cave entrance collapses!")