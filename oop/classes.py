# creates object of dog
# obj1 = dog()

# can set variables unique to the object
# obj1.name = "woof"
# obj1.age = 5

# if method exists on object you can call it
# obj1.bark()

# can have multiple objects, can be of same type
# obj2 = dog()
# obj3 = dog()
# obj4 = bird()

# Class declarations
class Dog:
    name = ""
    age = 0

    def bark(self):
        print("Bark")

# self in this class refers to the object itself like "this" in javascript

# __init__ is the constructor for each class it is called when creating an object
class Website:
    def __init__(self, title):
        self.title = title

    def show_title(self):
        print(self.title)

obj = Website('pythonbasics.org')
obj.show_title()