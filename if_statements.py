x = 3
if x < 10:
    print('x below 10')

if x > 10:
    print('x is greater than ten')

if x > 1 and x < 4:
    print('x is in range')

gender = input("gender? ")
gender = gender.lower()

if gender == 'male':
    print("your cat is male")
elif gender == 'female':
    print("your cat is female")
else:
    print("invalid input")

age = int(input("Age of your cat? "))
if age < 5:
    print("your cat is young")
else:
    print("your cat is an adult")

# more elegant and Pythonic way to do if statement blocks:
x = 3
if x == 2:
    print('two')
if x == 3:
    print('three')
if x == 4:
    print('four')
