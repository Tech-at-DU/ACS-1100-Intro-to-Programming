'''
Let's practice using .readline()!

.readline() reads one line from the file and returns it. 

The next time you use .readline() again, it will pick up where it left off.
'''

# STEP 1: Store file name in a variable
input_file_name = 'languages.txt'

# STEP 2: Open the file in read mode ('r')
infile = open(input_file_name, "r")

# STEP 3: 

# Using a for loop and .readlines(), we can read and print the first 5 lines of the file.

for i in range(5):
  line = infile.readline()
  print(line)

# TODO: To avoid double spacing, change the print statement to: print(line, end='')

# TODO: Read lines 4 to 15



# STEP 4: Close the file (We will learn about this the next few slides!)
infile.close()