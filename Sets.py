# Problem 1
"""Create  set called mySet that has three elements in it."""
myset = {'myName', 'Sushant', 427}
print(myset)

# Problem 2
"""Add the string 'pepper' to the following set
species = {'Maple bacon', 'Barbecue', 'Steak', 'Chilli'}"""
species = {'Maple bacon', 'Barbecue', 'Steak', 'Chilli'}
# species.update(["pepper"])
species.add("pepper")
print(species)

# Problem 3
"""Calculate the length of the string
    easternCanadaProvinceCapitals = {'Ottawa', 'Fredericton', 'Quebec City', 'Halifax', 'Charlottetown', 'St. Jons'}"""
easternCanadaProvinceCapitals = {'Ottawa', 'Fredericton', 'Quebec City', 'Halifax', 'Charlottetown', 'St. Jons'}
print(len(easternCanadaProvinceCapitals))

# Problem 4
"""Remove the Moscow from the following set
    westernCanadaProvinceCapitals = {'Vancouver', 'Saskatoon', 'Regina', 'Calgary', 'Moscow'}"""
westernCanadaProvinceCapitals = {'Vancouver', 'Saskatoon', 'Regina', 'Calgary', 'Moscow'}
westernCanadaProvinceCapitals.remove("Moscow")
print(westernCanadaProvinceCapitals)
