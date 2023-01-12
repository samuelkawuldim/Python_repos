# average of list of numbers

numbers = [25, 50, 75, 100, 125]

average = sum(numbers)/len(numbers)

print(round(average, 3))


print("curent and previous numbers and their sum in the range(10)")
previous_num = 0

# loop for 1 to 10
for i in range(1, 11):
    x_sum = previous_num+i
    print("curent number", i, " previous_num", previous_num, "sum: ", x_sum)
    # modify previous number
    # set it to the curent number
    previous_num = i
