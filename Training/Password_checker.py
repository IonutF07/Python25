#Password checker login program
print("Hello user!\n")
#variables
username="Ionut"
password="HardPass123"
login_attempts=0

while login_attempts <= 2:
    attempt_username=input("Please enter your username: ")
    attempt_password=input("type in your password: ")

    if attempt_username==username and attempt_password==password:
        print("You entered the correct username and password\n")
        print("Thank you for logging in")
        break
    else:
        print("You entered the incorrect username or password")
        login_attempts+=1

        print("Your account is blocked now\n")
        print("To unlock your account, create a new password")
        new_password=input("Please enter your new password: ")
        repeat_new_password=input("Confirm your new password: ")

        if new_password==repeat_new_password:
            password=new_password
            print("New password is: {}".format(password))
        else:
            print("New password is diffrent")