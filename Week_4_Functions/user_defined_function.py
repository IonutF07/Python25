def user_name():
    print("What is your name?")
    name = input()
    return name

user=user_name()
print(f"Hello, {user}!")