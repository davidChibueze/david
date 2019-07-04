#Problem set 3
#The python code checks for the number of times "bob" appears in a string
#s="thebobbobobthek"	
count = 0

for i in range(len(s)):
	if s[i:i+3] == "bob":
		count += 1
		
print("Number of times bob occurs is: ",count)
		