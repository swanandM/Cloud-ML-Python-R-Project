from Tkinter import *
from subprocess import call
import ttk
import os
import sys

def takeGRE():
	temp = test.get()
	print temp	

def GeneralAnalysis():
	firstWindow.destroy()
	call(["Rscript","general_analysis.R"])
	print "OUTPUT IS IN THE WORKING DIRECTORY"
def SpecificAnalysis():
	firstWindow.destroy()
	call(["python","SpecificAnalysis.py"])	

def UnivPredic():
	firstWindow.destroy()
	GRE = raw_input("Please input the GRE:")
	call(["Rscript","input.R",str(GRE)])
	
	
firstWindow = Tk()
firstWindow.title("Lets make life for a student easy")
firstWindow.geometry("500x300+400+250")
label1 = Label(firstWindow,text ="Welcome to the GRE-student help program")
label1.pack(pady=10)
label2 = Label(firstWindow,text = "Please select what type of help you require")
label2.pack(pady=10)
check1 = Button(firstWindow,text = "General Analysis    ",command = GeneralAnalysis)
check1.pack(pady=10)
check2 = Button(firstWindow,text = "Specific Analysis   ",command = SpecificAnalysis)
check2.pack(pady=10)
check3 = Button(firstWindow,text = "University Suggestor",command = UnivPredic)
check3.pack(pady=10)
firstWindow.mainloop()
