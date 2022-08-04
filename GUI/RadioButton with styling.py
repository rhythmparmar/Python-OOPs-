from tkinter import *
from tkinter.ttk import *
master=Tk()

master.geometry("300x500")

def selectedValue():
    print(v.get())


# Tkinter string variable
# able to store any string value
v=StringVar(master,"1")


# style class to add style to radiobutton
# it can be used to style any ttk widget
style=Style(master)
style.configure("TRadiobutton", background="light green",foreground="red", font=("arial",10,"bold"))


# Dictionary to create multiple buttons
values={"radioButton 1":"1",
        "radioButton 2":"2",
        "radioButton 3":"3",
        "radioButton 4":"4",
        "radioButton 5":"5"}


# Loop is used to create multiple radiobuttons
# rather than creating each button seperately
for(text, value)in values.items():
    Radiobutton(master, text=text, variable=v,value=value).pack(side=TOP,ipady=10,pady=5)

btn=Button(master, text="submit",command=selectedValue).pack()

master.mainloop()
