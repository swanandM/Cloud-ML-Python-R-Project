import re
import sys
import os

def Remove(UnivName):
	toRemove=["of","Of","at","At","the","The","-",","]
	result = ''
	for words in UnivName.split():
		if words not in toRemove:
			result = result + words + ' '
	return result

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


test = raw_input("Give the Univ name :")
test = Remove(test)
test = regex(test)
'''call([./PUT SCRIPT NAME HERE])'''
