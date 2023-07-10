persons = [ "John", "Marissa", "Pete", "Dayton" ]
restaurants = [ "Japanese", "American", "Mexican", "French" ]

for person in persons:
    for restaurant in restaurants:
        print(person + ' eats ' + restaurant)

# prints:
# John eats Japanese
# John eats American
# John eats Mexican
# John eats French
# Marissa eats Japanese
# Marissa eats American
# Marissa eats Mexican
# Marissa eats French
# Pete eats Japanese
# Pete eats American
# Pete eats Mexican
# Pete eats French
# Dayton eats Japanese
# Dayton eats American
# Dayton eats Mexican
# Dayton eats French
