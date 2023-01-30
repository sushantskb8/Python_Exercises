# Q Create a function in Python
"""Write a program to create a function that takes two arguments, name and age, and print their value"""
# def func(name, age):
#     print("My name is", name, "and I am ", age, "years old")
# func("Sushant", 20)

# Q Create a function with variable length of arguments
"""Write a program to create function func1() to accept a variable length of arguments and print their value."""
# def func1(*args):
#     for i in args:
#         print(i)
# print("Printing the values")
# func1(20, 40, 30)

# Q Return multiple values from a function
"""Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call"""
# def calculate(* const):
#     add = const[0] + const[1]
#     sub = const[0] - const[1]
#     return add, sub
# res = calculate(2,2)
# print(res)

# Q Create a function with a default argument
"""Write a program to create a function show_employee() using the following conditions.
    --> It should accept the employee’s name and salary and display both.
    --> If the salary is missing in the function call then assign default value 9000 to salary"""
# def show_employee(name, salary = 9000):
#     print("The employee name is", name)
#     print("Monthly salary is", salary)
# show_employee("Sushant", 190000)
# show_employee("Ruturaj")

# Q Create an inner function to calculate the addition in the following way
"""Create an outer function that will accept two parameters, a and b
    Create an inner function inside an outer function that will calculate the addition of a and b
    At last, an outer function will add 5 into addition and return it"""
# def calculate(a, b):
#     def add(a, b):
#         return a + b
#     addition = add(a, b)
#     return addition + 5
# res = calculate(2, 3)
# print(res)

# Q Assign a different name to function and call it through the new name
"""Assign a new name show_tudent(name, age) to it and call it using the new name."""
# def show_students(name, age):
#     print(name, age)
# show_students("Sushant", 20)
# show = show_students
# show_students("Sushant", 20)

# Q Generate a Python list of all the even numbers between 4 to 30
# li = []
# def list(num = 30):
#     for i in range(4, num + 1, 2):
#         li.append(i)
#     for i in range(4,num + 1, 2):
#         print(li)
#         break
# list()

# Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]
def great(x):
    for i in x:
        print(max(x))
        break
great(x)









