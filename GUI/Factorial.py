import tkinter as tk

root=tk.Tk()

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing number and Result
number_var=tk.IntVar()
result_var=tk.IntVar()


#defining a function that will
#get the nuumber and
#print them on the screen
def fact():
    number=number_var.get()

    print("The Number is: "+ str(number))

    f=1
    for i in range(1,number+1):
        f=f*i
    
    result_var.set(f)


# creating a label for
# number using widget label
number_label=tk.Label(root,text="Number", font=("calibre",10,"bold"))

# creating a entry for input
# number using widget entry
number_entry=tk.Entry(root,textvariable=number_var, font=("calibre",10,"normal"))


# creating a label for Result
result_label=tk.Label(root,text="Result",font=("calibre",10,"bold"))

# creating a entry for Result
result_entry=tk.Entry(root,textvariable=result_var,font=("calibre",10,"normal"))


# creating a button using a widget
# button that will call the Factorial function
sub_btn=tk.Button(root,text="Factorial",command=fact)

# placing the label and entry in
# the required position using grid method

number_label.grid(row=0,column=0)
number_entry.grid(row=0,column=1)
result_label.grid(row=1,column=0)
result_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

# performing an infinite loop for the window to display
root.mainloop()
