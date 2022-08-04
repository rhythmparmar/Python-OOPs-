from tkinter import *
from tkinter.ttk import *
root=Tk()
root.geometry("600x400")

name_var=StringVar()
gender_var=StringVar()
age_var=IntVar()
sr_citizen=StringVar()

def typeOfCitizen():
    if gender_var.get()=="Male":
        if age_var.get()<60: 
            msg=name_var.get()+" is not a senior citizen"
        else:
            msg=name_var.get()+" is a senior citizen"

    if gender_var.get()=="Female":
        if age_var.get()<55:
            msg=name_var.get()+" is not a senior citizen"
        else:
            msg=name_var.get()+" is a senior citizen"
    sr_citizen.set(msg)



name_label=Label(root,text="Name:",font=("lucida calligraphy",10,"bold"))
name_entry=Entry(root,textvariable=name_var,font=("lucida calligraphy",10,"normal"))
gender_label=Label(root,text="Gender:",font=("lucida calligraphy",10,"bold"))

r1=Radiobutton(root,text="Male",variable=gender_var,value="Male")
r2=Radiobutton(root,text="Female",variable=gender_var,value="Female")

age_label=Label(root,text="Age:",font=("lucida calligraphy",10,"bold"))
age_entry=Entry(root,textvariable=age_var,font=("lucida calligraphy",10,"normal"))
citizen_btn=Button(root,text="type Of Citizen",command=typeOfCitizen)
citizen_entry=Entry(root,textvariable=sr_citizen,font=("lucida calligraphy",10,"normal"))

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
gender_label.grid(row=1,column=0)
r1.grid(row=1,column=1)
r2.grid(row=1,column=2)
age_label.grid(row=3,column=0)
age_entry.grid(row=3,column=1)
citizen_btn.grid(row=4,column=0)
citizen_entry.grid(row=4,column=1)

root.mainloop()
