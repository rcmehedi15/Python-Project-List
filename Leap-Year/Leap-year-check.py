year = int(input("Enter The Check Leap Year : "))

if year % 400 == 0:
    print("It's Leap Year")
elif year % 100 == 0:
    print("It's not a leap Year")
elif year % 4 == 0:
    print("It's Leap Year ")
else:
    print("It's not a Leap Year")