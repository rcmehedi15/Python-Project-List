import datetime
from playsound import playsound
alarmHour = int(input("Enter Hour:"))
alarmMinutes = int(input("Enter Minutes :"))
alarmAm = input("am / pm : ")

if alarmAm == "pm":
    alarmHour+=12
while True:
    if alarmHour==datetime.datetime.now().hour and alarmMinutes==datetime.datetime.now().Minutes:
        print("Playing ........")
        playsound("music.mp3")
        break