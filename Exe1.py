#Loops in python
# For loops
# for num in range(1, 10):
# print(num)

# example2
#name = "samuel"
# for i in name:
# print(i)


# looping with list
#students = ["samuel,happiness,richard"]
# for i in students:
# print(i)


#ages = [5, 10, 15, 20]
# for i in ages:
# if i == 15:
#print("hey welcome")
# else:
# print("welcome")

# for loop
# for num1 in range(1, 21):
# print(num1)

# Performing sum of first 10 numbers using for loops (0 to 9)
#sum = 0
# for i in range(1, 10):
#sum = sum+i
#print('the sum of the numbers is', sum)

# loop
#sum = 1
# for i in range(1, 21):
#sum = sum+1
#print('the sum of the numbers is', sum)


# Python program to illustrate while loop

count = 1
# while (count < 3):
#count = count+1
#print('Hey samuel')

#while (count<5): count+=1; print('Hey samuel welcome')


#Samuel = 1
# while (Samuel < 5):
# print(Samuel)
#Samuel = Samuel+1


#While (count>10)
#count = 10
# while count > 1:
#count - 1
# print(count)

# Condition: Print even and odd numbers between 1 to 10
# for i in range(1, 10):
# if i % 2 == 0:
#print('even number:', i)
# else:
#print('odd number:', i)


# Exercise 2
# You are developing a program for a teacher to grade his students,s exam,
# The program should prompt the teacher to enter the number of questions on the exam
# The number of question the student answer correctly, and
# The number of points each question is worth.
# The program should then calculate the student,s grade as a percentage, and
# Print out a message indicating whether the student passed or failed

# Solution:
# Get input from teacher

num_questions = int(
    input('what is the total number of question for the exam:'))
num_correct_answer = int(
    input('what is the total number of question the student answer correctly'))
points_per_questions = float(
    input('what is the points worth for each question'))


# Calculate the students number of points (by multiplying the number of questions by the points)
total_num_points = num_correct_answer * points_per_questions

# calculate the maximium number of points earn by students
max_num_points_earn = num_questions*points_per_questions

# calculate the student score
total_score = (total_num_points/num_questions)*100

# print the conditional statement
if total_score > 50:
    print('the student pass the exam')
else:
    print('the student failed the exam')
