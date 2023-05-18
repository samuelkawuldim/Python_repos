# list with different type
#nums = [25, 50, 75]
# print(nums[2:])


#a = [10, 20, 30, 40, 50]
# print(a)
#a[2] = "power on"
# print(a)
#b = a
# print(b)


# function to add and subtract numbers
# def add_sub(x, y):
#a = x+y
#b = x-y
# return (a, b)


#result1, result2 = add_sub(10, 20)
#print(result1, result2)


# propose a function for name and age

# def person(name, age):
# print(name)
# print(age)


#person('samuel', 30)

# propose a function that add multiple numbers
# def sum(a, *b):
#c = a
# for i in b:
#c = c+i
# print(c)


#sum(50, 50, 50)


# functions to pass multiple aguement

def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)


person('samuel', age=25, city='mumbai', mob=3013646541)
