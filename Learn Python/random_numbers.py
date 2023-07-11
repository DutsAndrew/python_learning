import random

# create random floating point
print(random.random())

# pick a random whole number between 0, 10
print(random.randrange(0, 10))

# pick a random floating point number between 0 and 10
print(random.uniform(0, 10))

# random float between 1, 10
print(random.uniform(1, 10))

def create_random():
  x = random.randrange(0, 100)
  return print(x)

create_random()

def generate_100_numbers():
  x = []
  for i in range(100):
    x.append(random.randrange(0, 100))

  return print(x)

generate_100_numbers()