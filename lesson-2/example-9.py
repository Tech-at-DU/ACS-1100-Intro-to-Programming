print("Welcome to the snowboard length calculator!")
height = input("Please enter your height in inches: ")

height = float(height) # Converts str to float! 

# Input sees the user input as a string
# Before we can calculate it, we need to convert it to the correct
# data type... in this case, height should be an float


print(f"The length of the snowboard you need is: {height * 2.54 * 0.88} cm")