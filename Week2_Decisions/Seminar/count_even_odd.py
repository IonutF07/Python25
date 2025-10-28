even_count = 0
odd_count = 0

n1 = int(input('Enter the first whole number: '))
n2 = int(input('Enter the second whole number: '))
n3 = int(input('Enter the third whole number: '))

for n in (n1, n2, n3):
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"\n There were {even_count} even and {odd_count} odd numbers.")

