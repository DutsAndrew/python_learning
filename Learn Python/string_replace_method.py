s = "Hello World"
s = s.replace("World", "Universe")
print(s) # prints Hello Universe

new_string = "Hello World World World"
new_string = new_string.replace("World", "Universe", 2)

print(new_string) # prints Hello Universe Universe World

string = "Hello World Universe World"
string = string.replace("World", "Apples", 2)
string = string.replace("Hello", "Goodbye")
string = string.replace("Universe", "Plate", 1)
print(string)

string = string.replace("Goodbye Apples Plate Apples", "Fatal Error")
print(string)