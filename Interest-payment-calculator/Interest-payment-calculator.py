def main():
    print("This is a monthly payment loan calculator ")
    print("")

    loan = float(input("Enter the loan Amount : "))
    apr = float(input("Enter the annual interest rate : "))
    years = int(input("Enter amount of year : "))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = loan * monthly_interest_rate / (1-(1 + monthly_interest_rate) ** (-amount_of_months) )

    print("The monthly payment for this loan is : " + str(monthly_payment))

main()