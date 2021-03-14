
from tkinter import *

def calculate_cost():
    """
    calculated Tax and Total cost
    """
    given_tax = int(cs_tax.get())
    given_cost = int(cost.get())

    calculated_tax = given_cost*given_tax/100
    calculated_total_cost = given_cost+calculated_tax
    
    display_tax_value.config(text = calculated_tax)
    total_cost_value.config(text = calculated_total_cost)


root = Tk()
root.title("TryCatch Tax Calculator")
root.geometry("500x250")

cost = StringVar()
cs_tax = StringVar() #country-state tax

tax = StringVar()
total_cost = StringVar()

tax = "0"
total_cost = "0"

title = Label(root, text="Tax Calculator",
               fg="Blue", font=("Arial", 20, 'bold')).place(x=150, y=10)

# Getting cost value
get_cost_label = Label(root, text="Cost : ",
               fg="Blue", font=("Arial", 20, 'bold')).place(x=100, y=70)
get_cost = Entry(root,textvariable=cost,width=15).place(x=190, y=80)

# Getting tax value
get_tax_label = Label(root, text="Tax(%) : ",
               fg="Blue", font=("Arial", 20, 'bold')).place(x=100, y=110)
get_tax = Entry(root,textvariable=cs_tax,width=15).place(x=190, y=120)

#Calulate button
btn = Button(master=root, text="calculate",fg="green", font=("Arial", 10, 'bold') ,command=calculate_cost).place(x=230,y=150)

#Displaying amount of tax to  be paid
tax_value = Label(root, text="Your tax : ",
               fg="black", font=("Arial", 15, 'bold')).place(x=30, y=200)
display_tax_value = Label(root, text="",fg="black", font=("Arial", 15, 'bold'))
display_tax_value.place(x=130, y=200)

#Displaying total amount to be paid with tax
total_cost_label = Label(root, text="Total cost : ",
               fg="black", font=("Arial", 15, 'bold')).place(x=250, y=200)
total_cost_value = Label(root, text=total_cost,
               fg="black", font=("Arial", 15, 'bold'))
total_cost_value.place(x=370, y=200)


root.mainloop()
