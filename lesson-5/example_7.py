# The random lib has functions for generating random values
import random 

# Use random to generate random numbers like this: 
print(random.randint(1, 6)) # print random number from 1 to 6

# TODO: Print a random number between 0 and 1


# TODO: Generate a random number between 0 and 1 
# If the number is 0 print "Heads" if not print "Tails"

# I hear Dungeons and Dragons is popular. It's an 
# RPG game. Characters are defined by characteristics 
# like strength, intelligence and desxterity.
# These stats have a value of 3 to 18. Thats a random 
# number from 1 to 6 three times 

# TODO: Write a function that generates three random
# numbers from 1 to 6 adds them together and returns 
# the results 

def roll3d6(): 
	return 0

# TODO: Characters have attributes of strength
# intelligence and dexterity each has a value of 3 - 18
# Define three variables str, int, and dex below
# Use your function to generate the values. 

str = roll3d6()
# define int and dex here

# TODO: Every character starts with amount of gold pieces
# gp is equal to 3 - 18 * 10. Write a function that returns 
# start gp. Use the function above to generate a number from 
# 3 to 18 multiply the value returned by 10 and return it. 
# It's imortant you use the other function here (DRY!)

def startingGP(): 
	return 0 # should return 3d6 * 10

# TODO: Define a variable for gp and assign it a value: 

gp = startingGP()

# TODO: If your strength is highest you should be a 
# fighter, if you intelligence is highest you should 
# be a wizard, if your dexterity is highest you should 
# play a rogue. 
# Print a characters best profesion below by looking 
# at the numbers you generated. 



