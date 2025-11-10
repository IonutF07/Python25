
target = int(input("How many bars should be charged?\n"))
bars = 0

while bars < target:
    bars = bars +1
    print(f"Charging: {'█' * bars}")
    if bars == target:
        print("\nBattery is fully charged.")