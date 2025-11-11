#Simple calculator that performs addition, subtraction, multiplication, and division based on user input.
a = int(input("Type in first number: "))
b = int(input("Type in second number: "))
c = -1

def add():
    result = a + b
    print(f"{a} + {b} = ",result)

def sub():
    if b < 0:
        d = b * c
        result = a + d
        print(f"{a} - {b} = {result}")
    else:
        result = a - b
        print(f"{a} - {b} = {result}")

def mul():
    result = a * b
    print(f"{a} * {b} = {result}")

def div():
    if b==0:
        print("Division by zero")
    else:
        result = a / b
        print(f"{a} / {b} = {result}")

def run():
    choice = input("Choose option: \n+ \n- \n* \n/\n")

    if choice == "+":
        add()

    elif choice == "-":
        sub()

    elif choice == "*":
        mul()

    elif choice == "/":
        div()

run()