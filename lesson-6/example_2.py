''''
Welcome to Jess + Joi's Dog Kennel 🦴

We babysit 7 dogs. 1 per day of the week.

For example: 
On Sunday (index 0), we dog sit Henry. 🐕‍🦺
On Friday (index 5), we dog sit Wuffles. 🐕
'''

# List of dog names

dogs = ["Henry", "Odin", "Rookie", "Shin", "Jenny", "Wuffles", "Nugget"]


# Today is Monday. Print the 5th element of the list called dog to 
# see which dog will be coming into the kennel. 
print(dogs[0])

# TODO: Print the dog to ot on Tuesday


# TODO: Print the dog to sot on Wednesday


# TODO: Print the dog to ot on Thursday


# TODO: Using negative indexing, print the name of the dog who will be the 
# last to visit the kennel this week. (i.e. last in the list)
print(dogs[-1])

# TODO: Using negative indexing print the dog to sit on Friday


# TODO: Using negative indexing print the dog to sit on Saturday


# TODO: Using negative indexing print the dog to sit on Sunday


# Joi and Jess want to split up the work at the kennel. Using list 
# slicing, assign Joi dogs from Sunday thru Tuesday, and assign Jess dog 
# from Wednesday to Saturday. Create variable joi_dogs and jess_dogs to 
# store results. Print results.

# listname[start:stop]

joi_dogs = dogs[0:3]
print(joi_dogs)

# TODO: Print the dogs that Jess will sit on Thurs, Fri, Sat, Sun


# num_visit stores the number of times a dog has visited our kennel. 
# Nugget is visiting for the first time, so his number of returning 
# visits is missing from num_visits. 
num_visit = [2, 3, 5, 2, 7, 6]
num_visit.append(1)

# Test your work. Print dog 7 and the number of visits

print(dogs[6])
print(num_visit[6])

# TODO: Append a new dog to the list (I know this breaks the on dog 
# per of the week thing) 

# TODO: Print the new dog's name

# TODO: The new dog has visited the kennel. Add a visit to the list. 

# TODO: Imagine it's a new week and the dog's have all visited one 
# more time. Increase each dog's visit by 1

num_visit[0] += 1

