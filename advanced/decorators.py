# A function can take a function as an argument (the function to be decorated) and return the same function with or without extension
# extending functionality is useful at times

# All things are objects in Python, including functions
# can look odd at first:
def hello():
    print("hello")

message = hello

# call new function
message() # hello

# a decorator takes a function, extends it and returns

def hello_function(func):
    def inner():
        print("hello ")
        func()
    return inner

def name():
    print("alice")

# hello_function is a decorator and is decorating name
obj = hello_function(name)
obj() # hello alice

# functions can be extended by wrapping them:
def who():
    print("alice")

def display(func):
    def inner():
        print("the current user is: ", end="")
        func()
    return inner

if __name__ == "__main__":
    my_obj = display(who)
    my_obj() # the current user is: alice

# syntactic sugar and cleaner version of the above:
# @ symbol allows you to use the decorator here
@hello_function
def name():
    print("alice")

if __name__ == "__main__":
    name() # hello alice

# parameters/arguments can be used with decorators:
def pretty_sumab(func):
    def inner(a, b):
        print(str(a) + "+" + str(b) + " is ", end="")
        return func(a, b)

    return inner

@pretty_sumab
def sumab(a, b):
    summed = a + b
    print(summed)

if __name__ == "__main__":
    sumab(3, 5) # 3+5 is 8

# example use cases

# example 1: execution time
import time

def measure_time(func):
    
    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        print("function took " + str(time.time()-t) + " seconds to run")
        return res
    
    return wrapper

@measure_time
def my_function(n):
    time.sleep(n)

if __name__ == "__main__":
    my_function(2) # function took 2.0020177364349365 seconds to run


# example 2: web apps
# when building a web app in flask you use them with routes

@app.route("/about")
def about_page():
    return "website about nachos"