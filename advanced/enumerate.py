# enumerate() function is a built-in function that returns an enumerate object.
# lets you get index of an element while iterating over a list

# In other languages you loop over the list to get the index, in Python you shouldn't do that, instead you use enumerate()
# In Python you can iterate over the list while getting the index and value immediately

# Syntax: (sequence, start=0)
# Output: ((0, thing[0]), (1, thing[1]), (2, thing[2]))

browsers = ['Chrome','Firefox','Opera','Vivaldi']

# create an enumerable and convert to list
x = list(enumerate(browsers))
print(x) # [(0, 'Chrome'), (1, 'Firefox'), (2, 'Opera'), (3, 'Vivaldi')]

# returned object can be treated like an iterator, so next() call will work
eObj = enumerate(browsers)
y = next(eObj)
print(y)
y = next(eObj)
print(y)

# Enumerate List
fruits = [ "Apple","Berry","Cherry" ]

for i, j in enumerate(fruits):
    print(i, j)

# Enumerate Tuple
fruits = [(15,"Fifteen"), (12,"Twelve"), (19,"Nineteen")]

for i, j in enumerate(fruits):
    print(i, j)

# for cleaner tuple unpacking:
# f being used in front of a string uses the format() method to evaluate the needed values and print() execution, without it, nothing will fill those placeholders
for i, (price, name) in enumerate(fruits):
    print(f"index {i}, price {price}, and name {name}")

# Enumerating a string
vegetable = "Carrot"
for i, j in enumerate(vegetable):
    print(i, j) 
# Returns:   
# 0 C
# 1 a
# 2 r
# 3 r
# 4 o
# 5 t

# Enumerate with a different start index
for i, j in enumerate(vegetable, start=2):
    print(i, j)
# Returns:
# 2 C
# 3 a
# 4 r
# 5 r
# 6 o
# 7 t

# Enumerate Dictionaries
# cannot enumerate dictionaries, because a dictionary is not a sequence, dictionary does not have an index and it's not always in the same order.
# to iterate over a dictionary, do:

d = {'a':1, 'b':2, 'c':3}

for k, v in d.items():
    print(k, v)
# Returns:
# a 1
# b 2
# c 3

