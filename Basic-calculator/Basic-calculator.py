def add(a,b):
    anwser = a + b
    print(str(a) + "+" + str(b) + "=" + str(anwser))
def sub(a,b):
    anwser = a - b
    print(str(a) + "-" + str(b) + "=" + str(anwser))
def mul(a,b):
    anwser = a * b
    print(str(a) + "*" + str(b) + "=" + str(anwser))
def div(a,b):
    anwser = a / b
    print(str(a) + "/" + str(b) + "=" + str(anwser))
 
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")

choice = input("Enter Your Choice A,B,C,D,E : ")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("Enter 1st Number : "))
    b = int(input("Enter 2nd Number : "))
    add(a,b)
elif choice == "b" or choice == "B":
    print("Subtraction")
    a = int(input("Enter 1st Number"))
    b = int(input("Enter 2nd Number"))
    sub(a,b)
elif choice == "c" or choice == "C":
    print("Multiplication")
    a = int(input("Enter 1st Number"))
    b = int(input("Enter 2nd Number"))
    mul(a,b)
elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("Enter 1st Number"))
    b = int(input("Enter 2nd Number"))
    div(a,b)
 
elif choice == "e" or choice == "E":
    print("Program Ended")
    quit()