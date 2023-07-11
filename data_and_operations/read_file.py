filename = 'functions.py'

# read all lines
with open(filename) as f:
    content = f.readlines()

print(content) # ['def current_year():\n', '    print("2023")\n', '\n', 'current_year()\n', '\n', 'def f(x, y):\n', '    return x*y\n', '\n', 'print(f(3, 4))\n', '\n', 'result = f(5, 10)\n', 'print(result)']

# read block, if file doesn't have new lines or is binary, read() is better
in_file = open(filename, 'r')
data = in_file.read()
in_file.close()

print(data) # prints:
# 
# def current_year():
#     print("2023")

# current_year()

# def f(x, y):
#     return x*y

# print(f(3, 4))

# result = f(5, 10)
# print(result)
