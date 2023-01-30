#Problem 1
"""Create a tuple with four elements in an integer. Name the tuples "my_first_tuple" """
my_first_tuple = (1, 2, 3, 4)
print(my_first_tuple)


#Problem 2
"""Create a tuple with three elements named my_second_tuple. Make the third elemnent a tuple. The other two a list in that tuple."""
my_second_tuple = (["myFirstList"], 2, "tuple")
print(my_second_tuple)


#Problem 3
"""Print the third element of the tuple
    a_tuple = ('one', 2,'three')"""
a_tuple = ('one', 2, 'three')
print(a_tuple[2])


#Problem 4
"""Determinate the index of 'Joe Mortana' in the following tuples 
    quaterbacks = ('Tom Brady', 'Joe Mortana', 'Michael Vick', 'Peyton Maning')"""
quaterbacks = ('Tom Brady', 'Joe Martana', 'Michael Vick', 'Pety Maning')
print(quaterbacks.index('Joe Martana'))

#Problem 5
"""Count the numbers of times '5miles' occurs int the following tuple
    runninglog = ('5miles', '3miles', '5miles', '10 miles', '26miles-marathon-baby')"""
runninglog = ('5miles', '3miles', '5miles', '10 miles', '26miles-marathon-baby')
print(runninglog.count('5miles'))
    