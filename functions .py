# def checkDivisibility(a, b):
# if a % b == 0:
#print("a is divisible by b")
# else:
#print("a is not divisible by b")


# Driver program to test the above the above function
# checkDivisibility(5, 2)#


# def my_name(name, age):
#print("my name is ", name)
#print('my age is', age)


# drive program to test the above function
#my_name('samuel', '39')

def happy_birthday():
    print('happy birthday samuel')


# annaymous function
# happy_birthday()


def incremant(number, by):
    return number+by


print(incremant(2, 1))


# functions that returns a value
def math_operation(num1, num2):
    add = num2+num2
    sub = num1-num2
    # returning a single value(add)
    return add, sub


# read return value as a single variable
#rere, mimi = math_operation(10, 7)
#print("the sum of the two numbers is:", rere)

# function to check a number is odd or even
def check_number(num):
    if num % 2 == 0:
        return True
    else:
        return False


# call function
print(check_number(5))


# functions to check if two numbers are divisible
def check_divisibility(a, b):
    if a % b == 0:
        return True
    else:
        return False


# call function
print(check_divisibility(10, 3))


# local variables
# a local variable is a variable that is decleared inside a function and is not accessible
# out of a function

def akum():
    a = 12
    print("this is a local variable ", a)


def emma():
    b = 10
    print("the variable is", b)
# call function
    print(akum)


# Global variable
y1 = 600


def acha():
    print(y1)


acha()


def blaise():
    y2 = y1+20
    print(y2-4)


# Write a Python function called calculate_factorial that takes a positive integer as input and calculates its factorial using a loop.
# The factorial of a number n is the product of all positive integers from 1 to n.ef calculate_factorial():

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)


print(calculate_factorial(3))
