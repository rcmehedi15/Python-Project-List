import subprocess
# getting meta data
meta_data = subprocess.check_output(['netsh','wlan','show','profiles'])
# decoding meta data
data = meta_data.decode('utf-8',errors='backslashreplace')
#splitting datta by line by line
data = data.split('\n')
# creating a list of profiles 
profiles = []

# traverse the data
for i in data:
    # find all user profile in each item
    if "all user profile" in i :
        #if found
        # split the item
        i = i.split(':')
        i = i[1]
        i = i[1:-1]
        profiles.append(1)
# print heading
print("{:<}".format("WiFi Name","Password"))
print("-----------------------------")
# traversing the profiles 
for i in profiles:
    # try catch block begins
    try:
        results = subprocess.check_output(['netsh','wlan','show','profiles',i,'key = clear'])
        results = results.decode("utf-8",errors="backslashreplace")
        results = results.split('\n')

        results = [b.split(":")[1][1:-1] for b in results if "key Content" in b]
        try:
            print("{:<30} | {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30} | {:<}".format(i,""))

    except subprocess.CalledProcessError:
        print("Encoding Error Occured")
