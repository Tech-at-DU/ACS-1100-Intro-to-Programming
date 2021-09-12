'''
Example 1: This while loop prints a counter from 0  to 99:
'''
# Initialized counter to 0 
counter = 1

# while loop executed if counter < 100
while counter < 100:

  # Prints current value of counter.
  print(f"Counter: {counter}")
  
  # Increments value of counter by 1.
  counter += 1


# What should I change the conditional statement to to include 100?

'''
Example 2: This code reapeatedly prompts the user to enter a number between 1 and 20 until user enters correct input.

Note: Comment code above and uncomment code below before running.
'''

response = int(input("Enter a number between 1 and 20: "))

# The while loop is executed when user enters a number that is not between 1 and 20. 
while response > 20 or response < 1:
  response = int(input("Enter a number between 1 and 20: "))

print(f"Great you entered: {response}")


