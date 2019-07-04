#Problem set 2
#The python code counts the number of times vowels appear in a given word

#s ="thebiggestboy"
count=0

for i in s:
	#s is the given string
	if i == "a" or i=="e" or i=="i" or i=="o" or i=="u":
		count += 1
		
print("Number of vowels: ",count)