'''
Let's practice using .read()!

.read() reads the entire file.

If want it to read a number of characters, pass the number (int) between the parentheses.
'''

# STEP 1: Store file name in a variable
input_file_name = 'languages.txt'

# STEP 2: Open the file in read mode ('r')
infile = open(input_file_name, "r")

# STEP 3: 
# Example: Using .read() read the first 100 characters of the file and print results

read_data = infile.read(5) # Read a number of characters
print(read_data)

entire_file = infile.read(3) # Remove the number to read the entire file
print(entire_file)

# STEP 4: Close the file (We will learn about this the next few slides!)
infile.close()