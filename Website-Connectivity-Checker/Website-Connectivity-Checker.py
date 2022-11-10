import urllib.request as urlilib

def main(url):
    print("Checking Connectivity : ")

    response = urlilib.urlopen(url)
    print("Connected to",url ,"Successfully")

    print("The response code was : ", response.getcode())

print("This is a site connectivity checker program ")
input_url = input("Enter the url of the site you want to check : ")

main(input_url)