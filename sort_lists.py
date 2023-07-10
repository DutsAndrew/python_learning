x = [3,6,21,1,5,98,4,23,1,6]
x.sort()
print(x) # prints [1, 1, 3, 4, 5, 6, 6, 21, 23, 98]

words = ["Be","Car","Always","Door","Eat" ]
words.sort()
print(words) # prints ['Always', 'Be', 'Car', 'Door', 'Eat']

# reverse order
y = [3,6,21,1,5,98,4,23,1,6]
y.sort()
y = list(reversed(y))
print(y)

# best way to sort a list in reverse order
words = words[::-1]
print(words) # prints ['Eat', 'Door', 'Car', 'Be', 'Always']