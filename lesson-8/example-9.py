'''
Let's practice appending to files.

In append mode, we can use the .write() and .writelines() to append 
to the end of the file without overwriting existing data. 
'''
# STEP 1: Store file name in a variable
output_file_name = 'output.txt'

# STEP 2: Open the file in append mode ('a')
outfile = open(output_file_name, "a")


# STEP 3: Some teams were missing from the team of lists in output.txt. 
# Let's add some of the missing teams

teams = [
"Miami Dolphins\n",
"Minnesota Vikings\n",
"New Orleans Saints\n"
]

# appends the list of teams to the existing list.
outfile.writelines(teams)
  

# TODO: Append 3 more NFL Football teams to the file. Here is a 
# list: https://www.alphalists.com/list/alphabetical-list-nfl-teams



# STEP 4: Close the file (We will learn about this the next few slides!)



# STEP 5: Close the file
outfile.close()