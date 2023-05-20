# Using the print() function, print to the console: 'Learn Python!'
print('learn python')
# print function takes a parameter
print(2)

# Assign to the variable age number 20.
# Using the age variable and the print() function print to the console the following text:

# I am 20 years old.
age = 20
print("i am", age, "years old")
print('i am ' + str(age))
print(f"i am  {age} years old")

# Using these variables and the print() function, print to the console the following text:
# i am learning Python version 3.8


name = "python"
num = 3.8
print("i am learning " + name + " version " + str(num))


# Assign 199.99 to the price variable and check the solution.
# price =
# print('This costs', price)
# Expected Result - This costs 199.99

price = "199.99"
print("This costs " + str(price))


# Assign two variables that store the following values:

# $ 34.99 - product price (float)

# 20 lbs - product weight (int)

# Using the f-string formatting style print to the console the following message:

# Price: $34.99. Weight: 20 lbs.

product_price = float(34.99)
product_weight = int(20)
print(f"price: ${product_price}. weight:{product_weight} ibs")


# Below is an approximation of pi:

# pi = 3.1415926535

# Using f-string formatting, print the approximation of pi to two decimal places as shown below.

# Expected result:

# Pi: 3.14

pi = 3.1415926535
print(f"approximate of pi:{round(pi,2)}")
print(f'Pi: {pi:.2f}')
