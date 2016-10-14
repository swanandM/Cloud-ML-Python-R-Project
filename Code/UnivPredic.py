
from Tkinter import *
from subprocess import call
import ttk
import os


def takeGRE():
	temp = test.get()
	print temp	

def back():
	global Predic
	Predic.destroy()
	call(["python","Master.py"])

Predic = Tk()
test = IntVar()
Predic.title("University Suggestor")
Predic.geometry("500x300+400+250")
label3 = Label(Predic, text = "Here we will be suggesting a list of universities according to you GRE " )
label3.pack(pady = 10)
label4 = Label(Predic, text = "Please enter your GRE score:" )
label4.pack(pady = 10)
input_user = Entry(Predic,textvariable = test)
input_user.pack(pady = 10)
go = Button(Predic,text = "GO   ",command = takeGRE).pack(pady = 10)
back = Button(Predic,text = "Back",command = back).pack(pady = 10)
Predic.mainloop()