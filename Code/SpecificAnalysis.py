from Tkinter import *
from subprocess import call
import ttk
import os
import re



def back():
	global spfcAna
	spfcAna.destroy()
	call(["python","Master.py"])

def go():
	input_UnivName = univName.get()
	input_GRE = GRE.get()
	input_decision = decision.get()
	input_Season = Season.get()
	input_UnivName = change(input_UnivName)
	input_decision = (change(input_decision)).title()
	input_degree = degree.get()
	input_Season = (input_Season[0]).upper() + input_Season[-2:]
	if (input_UnivName != '' and input_GRE != 0 and input_decision != '' and input_Season != '' and  input_degree != ''):
		call(["Rscript","selective_option1.R",input_UnivName,str(input_GRE),input_decision,input_Season,input_degree])
	elif (input_UnivName == '' and input_GRE != 0 and input_decision != '' and input_Season != '' and  input_degree != ''):
		print ("Calling second")
		call(["Rscript","selective_option2.R",str(input_GRE),input_decision,input_Season,input_degree])
	elif (input_UnivName != '' and input_GRE == 0 and input_decision != '' and input_Season != '' and  input_degree == ''):
		print ("calling third")
		call(["Rscript","selective_option3.R",input_UnivName,input_decision,input_Season])
	#elif (input_UnivName != '' and input_GRE == 0 and input_decision != '' and input_Season != '' and  input_degree != ''):
		#print ("calling Fourth")
		#call(["Rscript","selective_option4.R",input_UnivName,input_decision,input_Season,input_degree])


def change(change_input):
	test =  change_input
	test = Remove(test)
	test1 = regex(test)
	test2 = test1.lower()
	return test2

def regex(UnivName):
    reg1 = re.compile(r'-')
    UnivName = re.sub(reg1,"",UnivName)
    reg1 = re.compile(r',')
    UnivName = re.sub(reg1,"",UnivName)
    reg = re.compile('\([^)]*\)')
    UnivName = re.sub(reg,"",UnivName)
    pattern = re.compile(r'\s+')
    UnivName = re.sub(pattern, '', UnivName)
    return UnivName

def Remove(UnivName):
	toRemove=["of","Of","at","At","the","The","-",","]
	result = ''
	for words in UnivName.split():
		if words not in toRemove:
			result = result + words + ' '
	return result

spfcAna = Tk()
univName = StringVar()
GRE = IntVar()
degree = StringVar()
decision = StringVar()
Season = StringVar()
spfcAna.title("Specific Analysis")
spfcAna.geometry("600x700+200+250")
label3 = Label(spfcAna, text = "This is a Specific Specific Analysis" )
label3.pack(pady = 10)
label4 = Label(spfcAna, text = "Please enter the following:" )
label4.pack(pady = 10)
lable5 = Label(spfcAna,text = "Enter the University Full name:")
lable5.pack(pady = 10)
input1 = Entry(spfcAna,textvariable = univName)
input1.pack(pady = 10)
lable6 = Label(spfcAna,text = "Enter the GRE:")
lable6.pack(pady = 10)
input2 = Entry(spfcAna,textvariable = GRE)
input2.pack(pady = 10)
Radiobutton(spfcAna, text="Accepted",padx = 20, variable=decision,value="Accepted").pack(pady= 8)
Radiobutton(spfcAna, text="Rejected",padx = 20, variable=decision,value="Rejected").pack(pady= 8)
#lable7 = Label(spfcAna,text = "Enter the Decision (Accepted/Rejected):")
#lable7.pack(pady = 10)
#input3 = Entry(spfcAna,textvariable = decision)
#input3.pack(pady = 10)
lable5 = Label(spfcAna,text = "Enter the acceptance Term")
lable5.pack(pady = 10)
input4 = Entry(spfcAna,textvariable = Season)
input4.pack(pady = 10)
Radiobutton(spfcAna, text="PhD",padx = 20, variable=degree,value="PhD").pack(pady= 8)
Radiobutton(spfcAna, text="MS",padx = 20, variable=degree,value="MS").pack(pady= 8)
go = Button(spfcAna,text = "GO   ",command = go).pack(pady = 10)
back = Button(spfcAna,text = "Back",command = back).pack(pady = 10)
spfcAna.mainloop()