'''
Let's practice using .readlines()!

.readlines() reads and returns a list of lines from a file.
'''

# STEP 1: Store file name in a variable
filename = 'languages.txt'

# STEP 2: Open the file in read mode ('r')
infile = open(filename, 'r')

# STEP 3: Use .readlines to get a lists of lines read from the file. 
lines = infile.readlines()

# This is a list of strings
print(lines)


# Calculate the length of list of lines
file_length = len(lines) 
print(file_length)

# Get the line at index 320 and print it.

# print(lines[320])

# TODO: Go to language.txt to check if correct.


# TODO: Print lines 184 to 190


# STEP 4: Close the file (We will learn about this the next few slides!)

infile.close()
