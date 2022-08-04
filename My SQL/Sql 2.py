from tkinter import *
from tkinter.ttk import *
import mysql.connector as sqltor
root=Tk()
root.geometry("600x400")

rollno_var=StringVar()
name_var=StringVar()


def addStudent():

    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="test")
    if mycon.is_connected()==False:
        print("Error connecting to MySQL database")
    else:
        r=rollno_var.get()
        n=name_var.get()

        
        Sql="Insert into Student values ({},'{}')".format(r,n)
        cursor=mycon.cursor()
        cursor.execute(Sql)
        mycon.commit()
        mycon.close()


rollno_label=Label(root,text="Roll Number: ", font=("calibre",10,"bold"))
rollno_entry=Entry(root,textvariable=rollno_var, font=("calibre",10,"normal"))
name_label=Label(root,text="Name: ",font=("calibre",10,"bold"))
name_entry=Entry(root,textvariable=name_var,font=("calibre",10,"normal"))

sub_btn=Button(root,text="Submit",command=addStudent)

rollno_label.grid(row=0,column=0)
rollno_entry.grid(row=0,column=1)
name_label.grid(row=1,column=0)
name_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()
