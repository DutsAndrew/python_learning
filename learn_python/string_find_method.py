s = "That I ever did see. Dusty as the handle on the door"
index = s.find("Dusty")
print(index) # prints 21
print(s[index:index+5]) # prints Dusty

# in keyword

if "Dusty" in s:
    print("query found")