#display the initial message
print("Calculate the sum of the first 100 numbers")
number = 1
total = 0
#use a while loop to calculate the sum
while number <= 100:
    total += number
    number += 1
#display the final result
print(f"The sum of the first 100 numbers is: {total}")