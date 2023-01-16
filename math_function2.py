# function that checks if a number ia an even or odd
def checkingnumbers(x):
    if x % 2 == 0:
        print(x, 'even number')
    else:
        print(x, 'odd number')


# test function
# checkingnumbers(50)


# function that checks your name
def greet(first_name, last_name):
    print(f"{first_name} {last_name}")
    print('welcome on board')


greet("Samuel", "Kawuldim")
