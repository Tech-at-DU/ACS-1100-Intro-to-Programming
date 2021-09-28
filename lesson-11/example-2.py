# Examine the code below. 
# What is it doing? 
# Could you make this code better? 

def printevens(x):
	y = 0
	while(y < len(x)):
		if y % 2 == 0:
			print(x[y], end=" ")
		y += 1
