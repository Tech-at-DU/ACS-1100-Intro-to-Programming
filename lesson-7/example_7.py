#TODO: Using a for loop, print out each color from the list called colors.
# colors = ["red", "orange", "green", "blue", "purple"]
          # [ 0,      1     ,   2   ,    3  ]
          

# for color in colors:  
#   print(color)

# For however many colors are in the list called colors
# exectute this for loop
# for i in range(len(colors)):
#   color = colors[i]
#   print(color + " is awesome!") 


#TODO: Create a list of 4 names.
#TODO: Using a for loop, print out each name with " is awesome!" added after each name.

names = ["John", "Jake", "Jessica", "Joi"]
for name in names:
  #print(name + " is awesome!")
  print(f"{name} is awesome!")

#TODO: create a list of five integers
#TODO: print the sum of the numbers in the list
numbers = [4, 6, 200, 32, 1]

total = 0
for num in numbers:
  total = total + num

print(total)

#TODO: After calulcating the sum, calculate the average.
# To calculate average, we take the sum divided by the number of elements in the list called numbers
avg = total / len(numbers)
print(avg)




# Redo these with range()