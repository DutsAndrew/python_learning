# Iterable - a Python object that can be uses as a sequence you can go to the next item using a next() method, you can loop over it, but can't access items directly
# Is a container object, can only return one of it's elements at a time

d = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5 }
iterable = d.keys()
print(iterable)

for item in iterable:
    print(item)

iterator = iter(iterable)
print(next(iterator))
print(next(iterator))

items = ["one", "two", "three", "four"]
iterator = iter(items)
x = next(iterator)
print(x)
