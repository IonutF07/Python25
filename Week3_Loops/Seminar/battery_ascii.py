
target = int(input("How many bars should be charged?\n"))
bars = 0

while bars < target:
    print("Charging: ", end="")
    bars = bars +1
    print("█ "* bars)

    print ("\n Battery is fully charged.")