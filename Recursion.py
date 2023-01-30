# Q Finding the factorial of a number
# n = int(input("Enter the number: "))
# def fac(n):
#     if (n == 0 | n == 1):
#         return n
#     else:
#         return n*(fac(n-1))
# res = fac(n)
# print(res)

# Q Fibonacci Series
# n = int(input("Enter the number: "))
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# for i in range(n):
#     print(fib(i), end=" ")

# Q Finding the power of a number
# def power(base, exp):
#     if exp == 0:
#         return 1
#     elif exp == 1:
#         return base
#     else:
#         return base*(pow(base, exp-1))
# base = int(input("Enter the base value: "))
# exp = int(input("Enter the vlaue of exponent: "))
# print("The answer of the above inputs is",power(base, exp))

# Combination
# nCr = n! / r! (n-r)!Combination
def fact(n):
    if n == 0 | n == 1:
        return 1
    else:
        return n * fact(n-1)
def combination(n, r):
    return fact(n) / (fact(r) * fact(n-r))

n = int(input("Enter the number: "))
r = int(input("Enter the value: "))
print(combination(n, r))