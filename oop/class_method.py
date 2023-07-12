# class method that's shared among all objects. To call a class method you put the class as the first argument.

# class methods can be called from instances and from the class itself.

class Fruit:
    name = "Fruitas"

    @classmethod
    def print_name(cls):
        print('The name is:', cls.name)

Fruit.print_name()

apple = Fruit()
berry = Fruit()

# can use class method with both objects and the class itself
Fruit.print_name()
apple.print_name()
berry.print_name()

# the parameter name now belongs to the class. If you change name by using an object it ignores it. But if you do that by the class it changes.
apple.name = "Apple"
Fruit.print_name() # Fruitas
apple.print_name() # Fruitas
berry.print_name() # Fruitas

Fruit.name = "Apple"
Fruit.print_name() # Apple
apple.print_name() # Apple
berry.print_name() # Apple

# Alternative way of writing a class method
class Veg:
    name = "Cucumber"

    def print_name(cls):
        print("The name is:", cls.name)

Veg.print_name = classmethod(Veg.print_name)

# Class method vs Static Method
# both don't need objects to be instantiated
# class method knows about the class as the class is parameter it takes
# static method doesn't know anything about the class
# class method gets the class when it's called and knows all the attributes and methods at this time