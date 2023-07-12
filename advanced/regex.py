import re

string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

matches = re.findall(r'woo\w*', string)
print(matches) # ['wood', 'woodchuck', 'woodchuck', 'wood']

if re.search(r'woo\w*', string):
    print("woo\w* found")
else:
    print("not found")

