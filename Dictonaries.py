# Problem 1
"""Create a dictionary with two elements. The keys should be lastname and firstname. the values should be your first
 name and last name."""
mydict = {
    'firstname' : 'Sushant',
    'latsname' : 'Bishoi'
}
print(mydict)

# Problem 2
"""Return the indian flag from the dictionary
    countryFlags = {
    'China' : 'chinese'
    'India' : 'indian'
    'United States' : 'united states'
    }"""
countryFlags = {
    'China' : 'chinese',
    'India' : 'indian',
    'United States' : 'united states'
    }
for i in countryFlags:
    print(countryFlags['India'])
    break


# Problem 3
"""Generate a list of all the keys from the following dictionary. Make sure it is a real (and not a different data   
 structure)"""
mydetails = {
    'firstname' : 'Sushant',
    'lastname' : 'Bishoi',
    'roll' : 427,
    'branch' : 'CSE'
}
print(mydetails)


# Problem 4
"""Generate a list of all the values from the following dictionary. Make sure it is a real list
 (and not a different data structure)"""
basketball = {
    'team' : input("Enter the name: "),
    'enrollNo' : int(input("Enter the enrolled number: "))
}
print(basketball)


# Problem 5
"""Remove all the elements from the dictionary"""
mydict.clear()
print(mydict)

# Problem 6
"""Remove Peter Power's entry from the phonebook dictionary  below"""
phoneBook = {
    'Aandrew' : 88554,
    'Emily Everett' : 454454,
    'Peter Power' : 454523,
    'Levis Lame' : 88978
}
phoneBook.pop('Peter Power')
print(phoneBook)