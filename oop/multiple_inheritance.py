# A class can inherit multiple super classes.
# Classes can inherit from multiple of classes in Python, not the case in other languages

# class can be named a subclass if it has several parents

# if a class inherits from super classes it will get all their attributes and methods. If you have 4 super classes it will inherit all of them.

# Format is:
# class Subclass(SuperClass1, SuperClass2, SuperClass3, SuperClass4):

# super class
class Human:
    name = ""

# super class
class Coder:
    skills = 3

# inherits both super classes above
class Pythonista(Human, Coder):
    version = 3

programmer = Pythonista()
programmer.name = "Alice"

print(programmer.name) # Alice
print(programmer.version) # 3
print(programmer.skills) # 3

# Criticism of using multiple inheritance is that classes are no longer re-usable and cannot be used easily again if a strong cohesion is built between classes with inheritance. This requires classes to be copied over with all of the super classes, which argues that there's probably a better way to write code than doing this.