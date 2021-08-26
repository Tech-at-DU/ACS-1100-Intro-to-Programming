#Scenario: You own an online store and want to send important messaging to the shopper.

# Shopping cart currently has 3 items that cost:
username = 'Joi'
item_1 = 2      # $2
item_2 = 10     # $10
item_3 = 11     # $11
cart_total = item_1 + item_2 + item_3

# Task 1️⃣ :
# Use f-strings , print a message to tell the user
# their total. Example: Joi's cart balance is 24.31
# print( f"{username}'s cart balance is {cart_total}")


# Task 2️⃣ :
# The minimum for free shipping is $25
# Using f-strings, print a message to tell the user
# how much they need to add to their cart total to qualify for free shipping

# Example: "Joi, you are $2 away from free shipping!"

# print(f"{username}, you are ${25 - cart_total} away from free shipping!")

"Joi's total is $22"
"Abba's total is $1200"

username = 'Abba'
total = 1000000000000

print(f"{username}'s total is ${total}")