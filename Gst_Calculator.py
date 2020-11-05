""""
Author: Abhay Gavandi
Name : GST Calculator
Version : 1.0.0
"""

from tkinter import *

#creating the appplication main window
top = Tk()

top.title("GST Calculator v1.0.0")

top.geometry("500x250")

#All TextVariable Entry
ta_input_entry = IntVar()
sgst_input_entry = IntVar()
sgst_input_percent_entry = IntVar()
igst_input_entry = IntVar()
igst_input_percent_entry = IntVar()
grt_input_entry = IntVar()


#Functionality

def calculate():
   ta_input_final = ta_input_entry.get()
   sgst_percent_final = sgst_input_percent_entry.get()
   igst_percent_final = igst_input_percent_entry.set(sgst_percent_final)
   sgst_input_set = float((int(ta_input_final))*(int(sgst_percent_final)/100))
   sgst_input_entry.set(sgst_input_set)
   igst_input_entry.set(sgst_input_set)
   grt_input_entry.set(float(ta_input_final+(sgst_input_set*2)))
    	
def clear_all():
    ta_input_entry.set("")
    sgst_input_entry.set("")
    sgst_input_percent_entry.set("")
    igst_input_entry.set("")
    igst_input_percent_entry.set("")
    grt_input_entry.set("")
	

#main Application

#Total Amount
ta = Label(top, text="Total Amount").place(x=30,y=30)

#SGST
sgst = Label(top, text="SGST            %").place(x=30,y=60)

#IGST
igst = Label(top,text="IGST             %").place(x=30,y=90)

#Grand Total
grt = Label(top,text="Grand Total").place(x=30,y=120)


#Input Channel

ta_input = Entry(top,text="",textvariable=ta_input_entry).place(x=170,y=30)

sgst_input = Entry(top,text="",state='disabled',textvariable=sgst_input_entry).place(x=170,y=60)

sgst_input_percent = Entry(top,text="",width=3,textvariable=sgst_input_percent_entry).place(x=65,y=60)

igst_input = Entry(top,text="",state='disabled',textvariable=igst_input_entry).place(x=170,y=90)

igst_input_percent = Entry(top,text="",state='disabled',width=3,textvariable=igst_input_percent_entry).place(x=65,y=90)

grt_input = Entry(top,text="",state='disabled',textvariable=grt_input_entry).place(x=170,y=120)

	
#Calculate 
cal = Button(top,command=calculate,text="Calculate",relief="sunken").place(x=30,y=150)


#Clear
clear_input = Button(top,command=clear_all,text="Clear",relief="sunken").place(x=100,y=150)


top.mainloop()
