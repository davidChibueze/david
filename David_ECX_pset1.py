#Problem set 1
#The python code below evaluates two variables varA and varB and determines if:
#a) A string is involved
#b) varA is bigger than varB
#c) varA is Equal to varB
#d) varA is smaller than varB

#varA, varB = 100, 200

if type(varA)==str or type(varB)==str:
	print("String involved")
else:
	if varA > varB:
		print("Bigger")
	if varA == varB:
		print("Equal")
	if varA < varB:
		print("Smaller")
