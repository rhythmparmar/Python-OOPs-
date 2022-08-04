from tkinter import *
from tkinter.ttk import *
root=Tk()

root.geometry("400x500")

name_var=StringVar()
submit_var=StringVar()
v=StringVar()

def selectedValue():

    msg = "Welcome "
    if v.get()=="Male":
        msg = msg + "Mr. " + name_var.get()
    else:
        msg = msg + "Mrs. " + name_var.get()
    submit_var.set(msg)




name_label=Label(root,text="Name",font=("lucida calligraphy",10,"bold"))
name_entry=Entry(root,textvariable=name_var,font=("lucida calligraphy",10,"normal"))

gender_label=Label(root,text="Gender",font=("lucida calligraphy",10,"bold"))



r1=Radiobutton(root,text="Male",variable=v,value="Male")
r2=Radiobutton(root,text="Female",variable=v,value="Female")


submit_btn=Button(root,text="Submit",command=selectedValue)
submit_entry=Entry(root,textvariable=submit_var,font=("lucida calligraphy",10,"normal"))

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
gender_label.grid(row=1,column=0)
r1.grid(row=1,column=1)
r2.grid(row=1,column=2)
submit_btn.grid(row=2,column=0)
submit_entry.grid(row=3,column=0)


root.mainloop()

