# unique to python languages like C++ or Java do not support this by default

# scoped variables are the same in Python as other languages, if they are in a function they are only visible by function
def complex_function(a, b):
    sum = a + b
    return sum

complex_function(2, 3)

# this function returns multiple variables
def get_persons():
    name = "Leona"
    age = 35
    country = "UK"
    return name, age, country

# destructuring of variables to get returns from get_persons() could set it as: a, b, c = get_persons() and gotten the same results
name, age, country = get_persons()
print(name)
print(age)
print(country)