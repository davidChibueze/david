#Problem set 4
#The python code checks for the longest substring in alphabetical order

#s="zyxwvutsrqponmlkjihgfedcbabcd"
i =""
temp=""
max=""
#for loop for obtaining the substrings in alphabetical order and placing them in a list box
for x in range(len(s)):
	if len(i)==0:
		temp = s[x]
	if len(i)==1:
		temp = s[x]
		if i>temp:
			if len(i)>len(max):
				max=i
				i = ""
			else:
				i=""
	if s[x]>=temp:
		i += s[x] 
		temp = s[x]
				
	if s[x]<temp:
		if len(i)>len(max):
			max=i
			i=""
			temp = s[x]
			i += s[x]
		else:
			i=""
			temp=s[x]
			i += s[x]	
if len(i)>len(max):
	max=i

print("Longest substring in alphabetical order is: ",max)

