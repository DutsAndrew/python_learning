# define strings                                                         
firstname = "Bugs"
lastname = "Bunny"

sequence = (firstname, lastname)
name = " ".join(sequence)
print(name) # prints Bugs Bunny

sequence_two = " ".join([firstname, lastname])
print(sequence_two) # prints Bugs Bunny

# can also join a list of words
words = ["How", "are", "you", "doing", "?"]
sentence = " ".join(words)
print(sentence)