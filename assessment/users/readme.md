# Assessment

Everyone is complaining about how complicated online banking is. We've made a new product that makes it easy! 

Data.txt has a list of users, their user names, and passwords. You need to write three functions. Each of your functions should take at least one parameter and return something. 

The goal is to read the file `data.txt` and build a list of users. Each line of this file has a user. This line has the username, password, full name, and balance. 

```
aman,1234,Andy Allman,1000
```

You can split this line on the `,` to get a list with each item.

```python
"aman,1234,Andy Allman,1000".split(',') # ["aman","1234","Andy Allman","1000\n"]
```

Notice string `split()` takes a delimeter (comma in this case ",") and splits the string on this character returning an array of substrings. From here you can access each element using the list syntax: 

```python
test = "aman,1234,Andy Allman,1000".split(',')
print(test[0]) # aman
print(test[1]) # 1234
print(test[2]) # Andy Allman
print(test[3]) # 1000
```

Your goal is to write a program that does the following: 

- Prompts for a user name 
- Prompts for a password 
- It should then look up the user matching both the user name and the password.
- Last it should print out the user's full name and account balance

Using your app might look something like this: 

```
Enter Name: aman     # prompts for user name
Enter password: 1234 # prompts for a password
Name: Andy Allman    # Displays Full name
Balance: 1000.0      # Displays Account balance
```

If the user name and password are not found it should print the message: "User name and password not found". It might look like this in the terminal: 

```
Enter Name: Test                 # Prompts for user name
Enter password: bogus            # Prompts for password 
User name and password not found # Displays error message
```

# Requirements 

Your program should load the data follow the descriptions above. 

You should write at least three functions. At least one function should take one or more parameters and return a value. Some suggestions: 

- Write a function to load data. Parameter: file name, returns a list of users.
- Write a function to display the user information. Parameters: one or more strings, or an array and return a formatted string. 
- Write a login function that takes username and password as parameters and returns a user dictionary. 

## Stretch Goals

If you have the above problems solved try these: 

### accrue interest

The accrue interest function takes an interest rate as a parameter. When called it loops over all users in the list and adds an amount to their balance equal to the current balance times the rate. 

### Deposit

Write a deposit function. This function should take the user name, password, and amount. It should search the list of users for the username and verify the password. If it finds a user it should add the amount to that user's account balance. 

### Withdrawl function

This function takes the user name, password, and amount. It should find the user name, verify the password and attempt to subtract the amount from the user's balance. If the amount is greater than the balance it should print an error. Otherwise, the amount is subtracted and the new balance is printed. 

### Transfer 

The transfer function takes a username, password, amount, and a second username. It should search for a user name, verify the password, subtract the amount from the first user's balance. If the amount is greater than the balance it should display an error. Otherwise, it finds the second user name in the list and adds the amount to their balance. 
