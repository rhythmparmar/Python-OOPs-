import tkinter as tk
root=tk.Tk()

root.geometry("600x400")


number_var=tk.IntVar()
result_var=tk.IntVar()


def fact():
    number=number_var.get()

    print("The Number is: "+ str(number))

    sum=0
    i=number
    while(i>0):
        r=i%10
        sum=sum+r
        i=i//10
        
    
    result_var.set(sum)


number_label=tk.Label(root,text="Number", font=("calibre",10,"bold"))
number_entry=tk.Entry(root,textvariable=number_var, font=("calibre",10,"normal"))

result_label=tk.Label(root,text="Result",font=("calibre",10,"bold"))
result_entry=tk.Entry(root,textvariable=result_var,font=("calibre",10,"normal"))

sub_btn=tk.Button(root,text="SOD",command=fact)


number_label.grid(row=0,column=0)
number_entry.grid(row=0,column=1)
result_label.grid(row=1,column=0)
result_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()
