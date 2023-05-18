# function that print out name
def my_name(samuel):
    print('my name is', samuel)


# call function using my name
my_name('samuel')


# functions that add two numbers and import the value
def add(x, y):
    results = x+y
    return results


n1 = int(input("enter the first number"))
n2 = int(input("enter the second number"))
res = add(n1, n2)
print(n1, "+", n2, "=", res)

# function that does budmas
a = float(input('enter the first number'))
b = float(input('enter the second number'))
add = a+b
sub = a-b
mul = a*b
div = a/b
print('addition is=', add)
print('subtraction is=', sub)
print('multiplication is=', mul)
print('division is =', div)
