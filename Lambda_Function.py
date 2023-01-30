# Q Write a lambda function that takes x as parameter and returns x+2. Then assign it to a variable named L.
# n = int(input("Enter the number: "))
# def myFun():
#     return lambda a: a + 2
# l = myFun()
# print(l(n))
# or
# x = 6
# l = lambda z: z+2
# print(l(x))


# Q Write a lambda function which takes z as a parameter and returns z*11
# n = int(input("Enter the number: "))
# res = lambda z: z*11
# print(res(n))

# Q Write a function which takes two arguments: a and b and returns the multiplication of them: a*b. Assign it to a
# variable named: f.
# res = lambda a,b : a * b
# print(res(2,2))

# Q Using .sort() method, create a lambda function that sorts the list in descending order. Refrain from using the
# reverse parameter. --> doubt

# This time use the sorted() function to sort the list in ascending order with lambda. -->doubt
lst=[100, 10, 10000, 1, 9, 999, 99]
print(sorted(lst, key=lambda x:x))

