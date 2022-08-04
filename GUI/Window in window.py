from tkinter import *
from tkinter.ttk import *
root=Tk()
root.geometry("600x700")


# Function to open a new window on a click of button
def openNewWindow():

    newWindow=Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("300x400")

    Label(newWindow,text="This is new window").grid(row=0,column=0)

label=Label(root,text="This is main window")
label.grid(row=1,column=0)

btn=Button(root,text="Click to open a new window",command=openNewWindow)
btn.grid(row=2,column=0)


root.mainloop()

    
