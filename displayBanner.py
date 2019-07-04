from time import sleep
from os import system
from random import randint

width = 79
message="Merry Christmas".upper()
printedWord=[""]*7
running=True
count=0

letters={
        "C":["  ***",
             " *   ",
             "*    ",
             "*    ",
             "*    ",
             " *   ",
             "  ***"],
             
        "M":["** **",
             "* * *",       
             "* * *",       
             "*   *",       
             "*   *",   
             "*   *",
             "*   *"],
             
        "E":["*****",
             "*    ",       
             "*    ",       
             "*****",       
             "*    ",   
             "*    ",
             "*****"],
             
        "A":["  *  ",
             " * * ",       
             "*   *",       
             "*****",       
             "*   *",   
             "*   *",
             "*   *"],
             
        "R":["***  ",
             "*  * ",       
             "*   *",       
             "*  * ",       
             "* *  ",   
             "*  * ",
             "*   *"],
             
        "Y":["*   *",
             "*   *",       
             " * * ",       
             "  *  ",       
             "  *  ",   
             "  *  ",
             "  *  "],
             
        "H":["*   *",
             "*   *",       
             "*   *",       
             "*****",       
             "*   *",   
             "*   *",
             "*   *"],
             
        "S":["*****",
             "*    ",       
             "*    ",       
             "*****",       
             "    *",   
             "    *",
             "*****"],
             
        "I":["*****",
             "  *  ",       
             "  *  ",       
             "  *  ",       
             "  *  ",   
             "  *  ",
             "*****"],
             
        "T":["*****",
             "  *  ",       
             "  *  ",       
             "  *  ",       
             "  *  ",   
             "  *  ",
             "  *  "], 
             
        " ":["     ",
             "     ",       
             "     ",       
             "     ",       
             "     ",   
             "     ",
             "     "],  
          
          

}
for row in range(7):
	for letter in message:
		printedWord[row]+=(str(letters[letter][row])+" ")
	
offset=width
print(len(printedWord[0]))

def blink():
	system("clear")
	#offset=randint(0,26)
	offset=randint(0,6)	
	mainRow= randint(0,30)
	for row in range(30):
		
		if row==mainRow:
			for Row in range(7):
				print(" "*offset,printedWord[Row][0:width-offset])
		else:
			print(" "*offset)
			
	sleep(5.0)
	

			
while running:
	system("clear")
	
	for row in range(7):
		print(" "*offset,printedWord[row][max(0,offset*(-1)):width-offset])
	
	offset -=1
	if offset<=(len(message)*7)*-1:
		offset=width
		count+=1
	if count==3:
		for i in range(3):
			blink()
		count=0
	sleep(0.05)	

		