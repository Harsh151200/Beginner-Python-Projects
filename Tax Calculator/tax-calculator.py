"""
Tax Calculator - 
    Asks the user to enter a cost and either a country or state tax. 
    It then returns the tax plus the total cost with tax.
"""
from tkinter import *
from tkinter import ttk
import pandas as pd

def calculate_cost():
    """
    calculated Tax and Total cost
    Takes Country name from ComboBox/Dropdown and finds correspoinf taxvalue in  Dataframe and calulates
    the values
    """
    given_country = cs_tax.get()
    given_tax = float(reader[reader["Country"] == given_country]["Tax"])
    given_cost = float(cost.get())

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

#Reading Country-Tax CSV File
reader = pd.read_csv("tax.csv")
countries = list(reader['Country'].values)

title = Label(root, text="Tax Calculator",
               fg="Blue", font=("Arial", 20, 'bold')).place(x=150, y=10)

# Getting cost value
get_cost_label = Label(root, text="Cost : ",
               fg="Blue", font=("Arial", 20, 'bold')).place(x=100, y=70)
get_cost = Entry(root,textvariable=cost,width=15).place(x=190, y=80)


# Getting tax value
get_tax_label = Label(root, text="Tax(%) : ",
               fg="Blue", font=("Arial", 20, 'bold')).place(x=100, y=110)
get_tax_box = ttk.Combobox(root,values=countries
                           ,textvariable=cs_tax
                           ).place(x=190,y=120)



#Calulate button
btn = Button(master=root, text="calculate",fg="green", font=("Arial", 10, 'bold') ,command=calculate_cost).place(x=230,y=150)


#Displaying amount of tax to  be paid
tax_value = Label(root, text="Your tax : ",
               fg="black", font=("Arial", 15, 'bold')).place(x=30, y=200)
display_tax_value = Label(root, text=tax,fg="black", font=("Arial", 15, 'bold'))
display_tax_value.place(x=130, y=200)



#Displaying total amount to be paid with tax
total_cost_label = Label(root, text="Total cost : ",
               fg="black", font=("Arial", 15, 'bold')).place(x=250, y=200)
total_cost_value = Label(root, text=total_cost,
               fg="black", font=("Arial", 15, 'bold'))
total_cost_value.place(x=370, y=200)

photo = PhotoImage(file = "Tax Calculator/tax.png")
root.iconphoto(False, photo)

root.mainloop()
