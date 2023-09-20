# Solve these problems again, but use the with keyword to close the files

# output_file_name = "candy.txt" 
# outfile = open(output_file_name, "a")


# candy = ['peppermints \n', 'york \n', 'nerds']
# outfile.writelines(candy)

# outfile.close()



# Example
with open("somefile.txt", "a") as outfile:
  mytext = ['something \n', 'to \n', 'say']
  outfile.writelines(mytext)

# TODO: Create a function that constians the block 
# above. This function should take a list of strings
# and append those strings to the file. 

# TODO: Add a parameter that is the file name. 
# With this addition you should be able to append any 
# text to any file! 
