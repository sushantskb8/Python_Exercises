# vowel = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
# strg = input("Enter the string: ")
# res = ""
# for i in strg:
#     if i in vowel:
#         res = res + i
# print(res)


# array = []
# n = int(input("Enter the number: "))
# print("Enter the array elements")
# for i in range(0, n):
#     print("Enter number at index ", i)
#     elements = int(input())
#     array.append(elements)
# print("The array is: ", array)
#
# x = int(input("Enter the year: "))
# if (x % 4 == 0) and (x % 100 != 0) or (x % 400 == 0):
#     print("It is  a leap year")
# else:
#     print("It is not a leap year")

# i = 1
# sum = 0
# n = 10
# while(i <= n):
#     sum = sum + i*i
#     i+=1
# print(sum)

# x = int(input("Enter the number: "))
# rev = str(x)
# print(rev)
# print(rev[::-1])

n1 = int(input("Enter First number :"))
n2 = int(input("Enter Second number :"))
x = n1
y = n2
while(n2!=0):
    t = n2
    n2 = n1 % n2
    n1 = t
gcd = n1
print(gcd)

