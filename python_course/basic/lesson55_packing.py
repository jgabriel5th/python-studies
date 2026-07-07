'''
Introduction to packing and unpacking
It's possible to unpack any iterable data type.
'''
# Unpacking:
# martialArts = ['Judo', 'Boxe', 'Taekwondo']
# martialArt1, martialArt2, martialArt3 = martialArts
# print(martialArt1) # Output: Judo
martialArt1, martialArt2, martialArt3 = ['Judo', 'Boxe', 'Taekwondo']
print(martialArt1)

# martialArt1, martialArt2, martialArt3, martialArt4 = ['BJJ', 'Kickboxing', 'Karate'] # It'll raise an exception called ValueError
# Because there are not enough values to unpack(too many variables).
# martialArt1, martialArt2 = ['BJJ', 'Kickboxing', 'Karate'] # It'll raise the same expection ValueError, but this time, there are
# too many values to unpack(not enough variables for them).

# How to unpack just one specific value from a list:
team1, *_ = ['Botafogo', 'Vasco', 'Flamengo', 'Fluminense']
print(team1, _)
# '_' is the variable that will pack the rest of the list.