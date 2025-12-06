print("What type of cover does the book have? (Hard/Soft)")
bookcover = input().strip().lower()
if bookcover == "hard":
    print("Books with hard covers can be more expensive!")
elif bookcover == "soft":
    print("Is the book perfect-bound? (yes/no)")
    perfect_bound= input().strip().lower()
    if perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stiches are great for short books")
