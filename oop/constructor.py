class Human:
    def __init__(self):
        self.legs = 2
        self.arms = 2

bob = Human()
print(bob.legs)

class Plane:
    def __init__(self):
        self.wings = 2

        #fly
        self.drive()
        self.flaps()
        self.wheels()

    def drive(self):
        print("Accelerating")

    def flaps(self):
        print("Changing flaps")

    def wheels(self):
        print("Closing wheels")

ba = Plane()
print(ba)

class Bug:
    def __init__(self):
        self.wings = 4

tom = Bug()

print(tom.wings)
print(bob.arms)
