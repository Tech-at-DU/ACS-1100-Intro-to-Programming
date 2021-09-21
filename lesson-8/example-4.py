'''
We can iterate over each line of a file using a for loop!

'''
# STEP 1: Store file name in a variable
input_file_name = 'languages.txt'

# STEP 2: Open the file in read mode ('r')
infile = open(input_file_name, "r")

# STEP 3: Files can be iterated over like a list. Use a for loop to iterate over the lines in a file.

for line in infile:
  print(line, end='')

# STEP 4: Close the file (We will learn about this the next few slides!)
infile.close()