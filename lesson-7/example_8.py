'''TODO: Prompt the user for their name. Then using while loops and conditional statements, sing them happy birthday. Your code should print the following:

Happy Birthday to you!
Happy Birthday to you!
Happy Birthday to {username}!
Happy Birthday to you!

'''

# Step 1: Prompt the user for their name.
username = input("What is your name?")

for i in range(4):
  if i == 2:
    print(f"Happy Birthday to {username}!")
  else:
    print("Happy Birthday to you!")