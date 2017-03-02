fullArray = ['H','H','H','H','H','T','T','T','T','T']

#returns a string version of an array
def toString(fullArray):
	full = "".join(fullArray)
	return full

#finds where in the array a space is located
def findSpace(fullArray):
	for x in range (0,len(fullArray)):
		 if fullArray[x] == "_":
			 return(x)

for c in range (0,5):
	x = input("Press space until you reach the left character of the two characters you want to move.\n" + toString(fullArray) +"\n")
	choice = len(x)

	#input check to make sure end of str or longer is not picked
	while choice >= len(fullArray) - 1:
		print("Please make a selection where the two coins are right next to each other.")
		x = input("Press space until you reach the left character of the two characters you want to move.\n" + toString(fullArray) +"\n")
		choice = len(x)

	#input check to make sure user choice does not include any spaces
	while fullArray[choice] == '_' or fullArray[choice+1] == '_':
		print("Please make a selection that doesn't include a '_'.")
		x = input("Press space until you reach the left character of the two characters you want to move.\n" + toString(fullArray) +"\n")
		choice = len(x)

	#first turn add user choice to end of array/string
	if c == 0:
		fullArray.extend([fullArray[choice],fullArray[choice+1]])

	#switches user choice with space
	else:
		temp1 = fullArray[choice]
		temp2 = fullArray[choice+1]
		space = findSpace(fullArray)
		fullArray[space] = temp1
		fullArray[space+1] = temp2
	fullArray[choice] = '_'
	fullArray[choice+1] = '_'

	#check for win condition
	if c == 4:
		if fullArray == ['_','_','H','T','H','T','H','T','H','T','H','T'] or \
		   fullArray == ['_','_','T','H','T','H','T','H','T','H','T','H'] or \
		   fullArray == ['H','T','H','T','H','T','H','T','H','T','_','_'] or \
		   fullArray == ['T','H','T','H','T','H','T','H','T','H','_','_',]:
			print("You WIN!")
		else: print("You LOSE!")
