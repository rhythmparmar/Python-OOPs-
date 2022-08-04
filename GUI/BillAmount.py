from tkinter import *
from tkinter.ttk import *
root=Tk()
root.geometry("600x500")
root.title("Clothing")

checkbox1=IntVar()
checkbox2=IntVar()
checkbox3=IntVar()

combobox1=IntVar()
combobox2=IntVar()
combobox3=IntVar()
bill_var=IntVar()
total_var=IntVar()
discount_var=IntVar()

def billAmount():
    t=0
    d=0
    if checkbox1.get()==1:        
        t=500*combobox1.get()

    if checkbox2.get()==1:
        t+=1000*combobox2.get()
    if checkbox3.get()==1:
        t+=2000*combobox3.get()

    

    if(t>=3000):
        d=t*0.1
    elif(t>=2000):
        d=t*0.05

    total_var.set(t)
    discount_var.set(d)    
    bill_var.set(t-d)
    
  

check_btn1=Checkbutton(root,text="Trouser",variable=checkbox1,
                       onvalue=1,offvalue=0,width=10)
check_btn2=Checkbutton(root,text="Jeans",variable=checkbox2,
                       onvalue=1,offvalue=0,width=10)
check_btn3=Checkbutton(root,text="Jacket",variable=checkbox3,
                       onvalue=1,offvalue=0,width=10)


combo_box1=Combobox(root,width=27,textvariable=combobox1)
trouser_label=Label(root,text="$500",font=("lucida calligraphy",10,"bold"))
combo_box2=Combobox(root,width=27,textvariable=combobox2)
jeans_label=Label(root,text="$1000",font=("lucida calligraphy",10,"bold"))
combo_box3=Combobox(root,width=27,textvariable=combobox3)
jacket_label=Label(root,text="$2000",font=("lucida calligraphy",10,"bold"))


combo_box1["values"]=("1",
                      "2",
                      "3")
combo_box2["values"]=("1",
                      "2",
                      "3")
combo_box3["values"]=("1",
                      "2",
                      "3")

sub_btn=Button(root,text="Submit",command=billAmount)

total_label=Label(root,text="Total: ",font=("lucida calligraphy",10,"bold"))
total_entry=Entry(root,textvariable=total_var,font=("lucida calligraphy",10,"normal"))

discount_label=Label(root,text="Discount: ",font=("lucida calligraphy",10,"bold"))
discount_entry=Entry(root,textvariable=discount_var,font=("lucida calligraphy",10,"normal"))

bill_label=Label(root,text="Bill Amount: ",font=("lucida calligraphy",10,"bold"))
bill_entry=Entry(root,textvariable=bill_var,font=("lucida calligraphy",10,"normal"))

check_btn1.grid(row=0,column=0)
combo_box1.grid(row=0,column=1)
trouser_label.grid(row=0,column=2)
check_btn2.grid(row=1,column=0)
combo_box2.grid(row=1,column=1)
jeans_label.grid(row=1,column=2)
check_btn3.grid(row=2,column=0)
combo_box3.grid(row=2,column=1)
jacket_label.grid(row=2,column=2)
bill_label.grid(row=3,column=0)
bill_entry.grid(row=3,column=1)
sub_btn.grid(row=4,column=1)
total_label.grid(row=5,column=0)
total_entry.grid(row=5,column=1)
discount_label.grid(row=6,column=0)
discount_entry.grid(row=6,column=1)

root.mainloop()




