# # Q Print First 10 natural numbers using while loop
# for i in range(0,11):
#     print(i)
# print()
#
# Q '''Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5'''
# row = int(input("Enter the value of row: "))
# for i in range(1, row + 1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()
#
# print()
#
# # Q Calculate the sum of all numbers from 1 to a given number
# '''Expected Output:
# Enter number 10
# Sum is:  55'''
#
# sum = 0
# num = int(input("Enter the number: "))
# for i in range(1, num+1, 1):
#     sum = sum + i
# print(sum)
#
# print()

# # Q Write a program to print multiplication table of a given number
# number = int(input("Enter the number: "))
# table = 1
# for i in range(1, 11,1):
#     result = i * number
#     print(number,'*',i,'=',result)
#
# print()

# # Q Display numbers from a list using loop
# # Write a program to display only those numbers from a list that satisfy the following conditions
# #
# # The number must be divisible by five
# # If the number is greater than 150, then skip it and move to the next number
# # If the number is greater than 500, then stop the loop
# # numbers = [12, 75, 150, 180, 145, 525, 50]
# '''Expected output:
# 75
# 150
# 145'''
#
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if(i > 500):
#         break
#     elif(i > 150):
#         continue
#     elif(i % 5 == 0):
#         print(i)
#
# print()

# # Q Display Fibonacci series up to 10 terms
# num1, num2 = 0, 1
# for i in range(10):
#     print(num1, end=' ')
#     res = num1 + num2
#     num1 = num2
#     num2 = res
#
# print()

# Q Find the factorial of a given number
# n = int(input("Enter the number: "))
# prod = 1
# i = 1
# if n < 0:
#     print("Invalid")
# elif(n == 0 | n == 1):
#     print(1)
# else:
#     while(i <= n):
#         prod = prod * i
#         i+=1
# print(prod)



# Q Printing the vowels of string
# vowel = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
# strg = input("Enter the string: ")
# res = ""
# for i in strg:
#     if i in vowel:
#         res = res + i
# print(res)

# Q Finding the value of cos series
n = int(input("Enter the number: "))
x = int(input("Enter the number: "))
s = 0
m = 1
for i in range(0, n + 1, 2):
    f = 1
    j = 1
    while(j <= i):
        f = f * i
        j = j + 1
    s = s + m * (pow(x, i)//f)
    m = m * (-1)
print(s)
