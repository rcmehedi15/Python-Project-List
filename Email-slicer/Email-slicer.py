def main():
    print("Welcome to Email Slicer ")
    print("")

    email_input = input("Enter Your Email Address :")
    (username,domain) = email_input.split("@")
    (domain,extension) = domain.split(".")

    print("Username : ",username)
    print("Domain : ",domain)
    print("Extension : ",extension)
main()