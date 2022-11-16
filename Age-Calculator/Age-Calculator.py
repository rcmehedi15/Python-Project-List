from tkinter import * 
from datetime import date

root=Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("Age Calculator")

#image

photo=PhotoImage(file="age.jpg")
myimage = Label(image=photo)
myimage.pack(padx=15,pady=15)

#logic of birthday
def CalculateAge():
    today=date.today()
    birthDate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year - birthDate.year-((today.month,today.day)<(birthDate.month,birthDate.day))
    Label(text=f"{nameValue.get()} your age is {age}",font=30).place(x=300,y=500)

#Show name,year,month,day
    
Label(text="Name",font=23).place(x=200,y=250)
Label(text="Year",font=23).place(x=200,y=300)
Label(text="Month",font=23).place(x=200,y=350)
Label(text="Day",font=23).place(x=200,y=400)

#string value print

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

#input box

nameEntry = Entry(root,textvariable=nameValue,width=30,bd=3,font=20)
nameEntry.place(x=300,y=250)

yearEntry = Entry(root,textvariable=yearValue,width=30,bd=3,font=20)
yearEntry.place(x=300,y=300)

monthEntry = Entry(root,textvariable=monthValue,width=30,bd=3,font=20)
monthEntry.place(x=300,y=350)

dayEntry = Entry(root,textvariable=dayValue,width=30,bd=3,font=20)
dayEntry.place(x=300,y=400)

#Button 
Button(text="Calculate Age",font=20,bg="black",fg="white",width=14,height=2,command=CalculateAge).place(x=300,y=450)

root.mainloop()
