# Q Finding the sum of first n natural numbers
# def sum(n):
#     if n <= 0:
#         return 0
#     else:
#         return n + sum(n - 1)
# n = int(input("Enter the number: "))
# print(sum(n))






# x = int(input("Enter the number: "))
# rev = str(x)
# print(rev)
# print(rev[::-1])



# Fibonacci series
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Enter the number: "))
for i in range(n):
    print(fib(i), end=' ')
