# import modules 
# pip install googletrans==3.1.0a0
# pip install tkinter
from tkinter import *
from tkinter import ttk,messagebox
from googletrans import Translator, LANGUAGES

# create a display window
root = Tk()
root.geometry('1080x400')

root.resizable(0,0)
root.config(bg = 'ghost white')

root.title("Google Translator By Md Mehedi Hasan")

Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg='blue1',fg='white',width='200').pack()

Label(root,text ="Rc Mehedi Hasan", font = 'arial 15 bold',fg='white', bg ='green' , width = '200').pack(side = 'bottom')


# Create an Input-output text widget

Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)

Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)

Label(root,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)

Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)

# Define Combobox to select the language

language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values= language, width =22)
src_lang.place(x=20,y=60)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=890,y=60)
dest_lang.set('choose output language')

# Define Function

def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())

    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

# Create a translate button
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'blue',fg='white')

trans_btn.place(x = 490, y= 180 )

root.mainloop()