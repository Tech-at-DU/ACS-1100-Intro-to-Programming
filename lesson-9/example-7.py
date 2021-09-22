'''
Let's see the items() and for loop in action :D
'''

fruit_count = {
	'Apple' : 10,
  'Pear'  : 5,
  'Mango' : 4 
}

print(fruit_count.items())
# [ ('Apple', 10), ('Pear', 5), ('Mango', 4) ]


for key, value in fruit_count.items():    
  print(f'Number of {key}: {value}')

# TODO: Define a new loop. Loop over the fruit_count 
# dictionary and add 4 to each count.




# TODO: Confirm this worked by printing fruit_count


inventory = {
	'Jordan 1' : 1,
	'Yeezy'    : 8,
	'Air Max'  : 10,
	'SB Dunk'  : 5,
	'Cortez'   : 20,
	'Jordan 6' : 100 
}


#TODO: Use a for loop to print out the key and value of 
# each item in the inventory dictionary
# Print f"You have {value} {key}"



