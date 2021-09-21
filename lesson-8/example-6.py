'''
Let's practice writing to a file using .write()!

.write() writes a string x to the file and returns number of characters written.

Note: You can only write string values to a file.
'''

# STEP 1: Store file name in a variable
output_file_name = 'output.txt'

# STEP 2: Open the file in write mode ('w')
outfile = open(output_file_name, "w")

# STEP 3: Write the quote from Justice Ruth Bader Ginsburg to the file. 

quote = "When will there be enough women on the court?' My answer is, 'When there are nine.'"


# TODO: Store line 17 into a variable called num_characters and print it to see how many characters were written to the file.  

num_char = outfile.write(quote)
print(num_char)


# STEP 4: Close the file (We will learn about this the next few slides!)
outfile.close()

