import random
import string
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()" )
def generate_password():
    password_length = int(input("How long would you like your password to be ?"))

    random.shuffle(characters)
    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)
option =  input("Do You want to generate a password ? (Yes/No) : ")

if option == "Yes":
    generate_password()
elif option == "NO":
    generate_password()
else:
    print("Invalid Input,Please input Yes Or No")
    quit()