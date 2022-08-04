from tkinter import *
root=Tk()
root.geometry("600x700")

submit_var=StringVar()
checkbutton1=IntVar()
checkbutton2=IntVar()
checkbutton3=IntVar()

def selectedValue():
    msg="Selected Items: "
    if checkbutton1.get()==1:
        msg+="Tutorial "
    if checkbutton2.get()==1:
        msg+="Student "
    if checkbutton3.get()==1:
        msg+="courses "

    submit_var.set(msg)
        

w=Label(root,text="Geeks For Geeks",font=("lucida calligraphy",20,"bold"))
w.grid(row=0,column=1)


Button1=Checkbutton(root,text="Tutorial",variable=checkbutton1,
                    onvalue=1,offvalue=0,height=2,width=10)

Button2=Checkbutton(root,text="Student",variable=checkbutton2,
                    onvalue=1,offvalue=0,height=2,width=10)

Button3=Checkbutton(root,text="Courses",variable=checkbutton3,
                    onvalue=1,offvalue=0,height=2,width=10)

sub_btn=Button(root,text="Submit",command=selectedValue)
sub_entry=Entry(root,textvariable=submit_var,font=("lucida calligraphy",10,"normal"))

Button1.grid(row=1,column=1)
Button2.grid(row=2,column=1)
Button3.grid(row=3,column=1)
sub_btn.grid(row=4,column=0)
sub_entry.grid(row=4,column=1)

root.mainloop()
