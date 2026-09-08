'''
Example 1: This while loop prints a counter from 1 to 99:
'''
# Initialized counter to 1 
counter = 1

# while loop executed if counter < 100
while counter < 100:

  # Prints current value of counter.
  print(f"Counter: {counter}")
  
  # Increments value of counter by 1.
  counter += 1


# To include 100, change the condition to `counter <= 100` (or `counter < 101`).

'''
Example 2: This code reapeatedly prompts the user to enter 
a number between 1 and 20 until user enters correct input.

Note: Comment code above and uncomment code below before running.
'''

response = int(input("Enter a number between 1 and 20: "))

# The while loop is executed when user enters a number that is 
# not between 1 and 20. 
while response > 20 or response < 1:
  response = int(input("Enter a number between 1 and 20: "))

print(f"Great you entered: {response}")

