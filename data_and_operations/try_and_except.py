# Python won't tell you about errors like syntax issues or grammar faults, it will abruptly stop, which is bad.
# You can use a try and except statement to properly deal with this, otherwise an emergency halt will happen

try:
    1 / 0
except ZeroDivisionError:
    print("Divided by zero")

print("Should reach here and bypass emergency halt")

try:
    open("fantasy.txt")
except:
    print("Something went wrong, file not found")

print("Should also reach here")


# try:
#     # code
# except FileNotFoundError:
#     # handle exception
# except IsADirectoryError:
#     # handle exception
# except:
#     # all other exceptions

print("Should reach here")

# Finally can be used if no exception is thrown
try:
    x = input("Enter number: ")
    x = x + 1
    print(x)
except:
    print("Invalid input")
finally:
    print("Valid input.")


def fail():
    1 / 0

try:
    fail()
except:
    print("Exception ocurred")

print("Program continued")

# This code doesn't run as f is declared in the try block and can't be scoped to finally, so this example from the tutorial does not work
# try:
#     f = open("test.txt")
# except:
#     print("could not open file")
# finally:
#     if f:
#         f.close()

print("Program continues again")

# Try else

# else clause is executed if no exception is raised
# Finally clause is ALWAYS executed
try:
    x = 1
except:
    print("Failed to set X")
else:
    print("No exception occurred")
finally:
    print("We always do this")

# ALL BUILT IN EXCEPTIONS:
# AssertionError	if assert statement fails.
# AttributeError	if attribute assignment or reference fails.
# EOFError	if the input() functions hits end-of-file condition.
# FloatingPointError	if a floating point operation fails.
# GeneratorExit	Raise if a generator's close() method is called.
# ImportError	if the imported module is not found.
# IndexError	if index of a sequence is out of range.
# KeyError	if a key is not found in a dictionary.
# KeyboardInterrupt	if the user hits interrupt key (Ctrl+c or delete).
# MemoryError	if an operation runs out of memory.
# NameError	if a variable is not found in local or global scope.
# NotImplementedError	by abstract methods.
# OSError	if system operation causes system related error.
# OverflowError	if result of an arithmetic operation is too large to be represented.
# ReferenceError	if a weak reference proxy is used to access a garbage collected referent.
# RuntimeError	if an error does not fall under any other category.
# StopIteration	by next() function to indicate that there is no further item to be returned by iterator.
# SyntaxError	by parser if syntax error is encountered.
# IndentationError	if there is incorrect indentation.
# TabError	if indentation consists of inconsistent tabs and spaces.
# SystemError	if interpreter detects internal error.
# SystemExit	by sys.exit() function.
# TypeError	if a function or operation is applied to an object of incorrect type.
# UnboundLocalError	if a reference is made to a local variable in a function or method, but no value has been bound to that variable.
# UnicodeError	if a Unicode-related encoding or decoding error occurs.
# UnicodeEncodeError	if a Unicode-related error occurs during encoding.
# UnicodeDecodeError	if a Unicode-related error occurs during decoding.
# UnicodeTranslateError	if a Unicode-related error occurs during translating.
# ValueError	if a function gets argument of correct type but improper value.
# ZeroDivisionError	if second operand of division or modulo operation is zero.

# User-defined Exceptions

# users can create their own exceptions, but must create a class that inherits from Exception
class LunchError(Exception):
    pass

# If you run the line below all other lines won't run because this throws an error which halts the program
# raise LunchError("Programmer went to lunch")

class NoMoneyException(Exception):
    pass

class OutOfBudget(Exception):
    pass

balance = int(input("Enter Balance: "))
if balance < 1000:
    raise NoMoneyException
if balance > 1000:
    raise OutOfBudget