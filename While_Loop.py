# # Q  Write a program in Python to display the Factorial of a number
# fact = 1
# n = int(input("Enter the number: "))
# while(n > 0):
#     fact = fact * n
#     n-=1
# print(fact)

# # Q Write a Python program to reverse a number
# n = int(input("Enter the number: "))
# rev = 0
# while(n!=0):
#     rem = n % 10
#     rev = rev * 10 + rem
#     n = n // 10
# print("The reverse of the number is: ", rev)

# # Q Write a program to print n natural number in descending order using a while loop
# n = int(input("Enter the number: "))
# while(n > 0):
#     print(n)
#     n -= 1

# # Q. Wap to find the sum of 1 + 4 + 9 + --- + 100
# i = 1
# sum = 0
# n = 10
# while(i <= n):
#     sum = sum + i*i
#     i+=1
# print(sum)

# # Q . Wap to find the gcd of two numbers
# n1 = int(input("Enter First number :"))
# n2 = int(input("Enter Second number :"))
# x = n1
# y = n2
# while(n2!=0):
#     t = n2
#     n2 = n1 % n2
#     n1 = t
# gcd = n1
# print(gcd)


# Q . Find a number is strong or not
# n = int(input("Enter the number: "))
# temp = n
# sum = 0
#
# while(n > 0):
#     i = 1
#     fact = 1
#     rem = n % 10
#     while(i <= rem):
#         fact = fact * i
#         i += 1
#     sum = sum + fact
#     n = n // 10
# if(sum == temp):
#     print("The number is strong number")
# else:
#     print("It is not a strong a number")

# Q Prime or not
# n = int(input("Enter the number: "))
# i = 2
# count = 0
# if n == 0 or n == 1:
#     count = 1
# while(i <= n/2):
#     if n % i == 0:
#         count = 1
#         break
#     i+=1
#
# if count == 0:
#     print("It is prime number")
# else:
#     print("It is not a prime number")