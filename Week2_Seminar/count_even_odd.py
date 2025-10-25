print("Enter the first whole number:")
first_num = int(input())
print ("Enter the second whole number:")
second_num = int(input())
print ("Enter the second whole number:")
third_num = int(input())
even_count = 0
odd_count = 0
if first_num % 2 == 0:
    if second_num % 2 == 0:
        odd_count += 1
    if third_num % 2 == 0:
        odd_count += 1
print (f"There were {even_count} even numbers and {odd_count} odd numbers.")
