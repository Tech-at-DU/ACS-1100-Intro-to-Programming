# Logical errors do not throw errors. They simply just dont return the result we were expecting.

temperature = int(input("What is the temp in Fahrenheit? "))

if temperature < 75:
  print("Whew. It is hot!")
else:
  print("Brrrr. It's cold.")