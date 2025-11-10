print("Towards each direction should i go (up,down,left,right)")
direction = input()
if direction == "up":
    print("I am moving in upward direction!")
if direction == "down":
    print("I am moving in downward direction!")
if direction == "left":
    print("I am moving to the left!")
if direction == "right":
    print("I am moving to the right!")
else:
    print("Unknown direction. Please choose up/down/left/right")