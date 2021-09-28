# Compare the two functions below. 
# Grade the code quality of each. 

# Function 1

def foo(x):
	y = 0
	for z in x:
		if z == 'e':
			y = y + 1
	if y == 2:
		return True
	else: 
		return False


# Function 2

def two_e(str):
	count = 0
	for char in str:
		if char == 'e':
			count += 1
	
	if count == 2: 
		return True
	else: 
		return False


