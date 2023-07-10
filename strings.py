x = "Hell0"
print(x)

# can index strings using blockquotes
print(x[0]) # prints H
print(x[1]) # Prints e

# using a colon can create a substring, if no number is written python assumes first or last character
hello_world = "hello world"

sub_string = hello_world[0:3]
print(sub_string) # prints hel

sub_string_two = hello_world[:3]
print(sub_string_two) # prints hel

sub_string_three = hello_world[3:] 
print(sub_string_three) # prints lo world

# more examples of string operations
nancy = "Nancy"
print(nancy)

number_and_text_string = "My lucky number is %d, what is yours?" % 7
print(number_and_text_string) # prints My lucky number is 7, what is yours?

number_and_text_string_two = "My lucky number is " + str(7) + ", what is yours?"
print(number_and_text_string_two) # prints My lucky number is 7, what is yours?

# print character by index
print(x[0])

#print piece of string
print(x[0:3])