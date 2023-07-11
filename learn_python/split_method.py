s = "Its to easy"
words = s.split()
print(words) # prints ['Its', 'to', 'easy']

# len() will give number of characters and number of words
print(len(words)) # prints 3
print(len(s)) # prints 11

# string to characters use list() instead
word = "Easy"
x = list(word)
print(x) # prints ['E', 'a', 's', 'y']