# Store the file name in a variable called filename
filename = 'music_playcounts.txt'

# Open the file in readmode
infile = open(filename, 'r')

#Using .readlines(), we will create a list where each
# element is a line from the file.
lines = infile.readlines()


# Create a dictionary and call it play_count

play_count = {}


for line in lines:

  # Removing the new line character from line
  stripped_line = line.strip()

  # Spliting string into two seperate strings
  split_line = stripped_line.split(',')
  
  # Access the key and value from the split line list
  key = split_line[0]
  value = split_line[1]

  # Added it to the dictionary called play_count
  play_count[key] = value


print(play_count)

# We are going to write some code to display play 
# counts for songs stored in a text file using a dictionary 

# This function will create and return the completed dictionary
def create_playcounts_dictionary(filename):

  #Read in the file contents and store to a list

  file_lines = open(filename, "r").readlines()

  #make an empty dictionary and save it to a variable
  #we are going to build up the keys and values from the file data 
  play_count_dictionary = {}
  #Loop through the lines, parse, and store


  for line in file_lines:
    split_line_list = line.rstrip().split(",")

    #get the song name as the key and the play count as the value
    song_name = split_line_list[0]
    play_count = split_line_list[1]

    # Adds to dictionary
    play_count_dictionary[song_name] = int(play_count)
  
  return play_count_dictionary

print(create_playcounts_dictionary("music_playcounts.txt"))

# TODO: Read the code here and ask yourself what it is trying to do

# TODO: Run the code and look at the output. Ask youself 
# What is different between the lines of code that were output?


