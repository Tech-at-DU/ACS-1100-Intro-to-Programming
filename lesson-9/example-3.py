'''
Let's practice accessing values from a dictionary!
To access a value, we access it using its key.

'''

# Imagine that a customer places the following order 
# at your empanada shop:

'''
Order:
1 cheese empanada
2 beef empanadas 
'''

menu = {"chicken": 1.99, "beef":1.99, "cheese":1.00, "guava": 2.50}

# Get the price of a guava empanada
guava_price = menu['guava']
guava_order = 7
print(f"guava_price: {guava_price} order: {guava_order} total: {guava_order * guava_price}")

# TODO: Using the dictionary called menu, access the prices 
# for cheese and beef. Print the prices to terminal. 



# TODO: Calculate the total price of the order 
# and print it.


