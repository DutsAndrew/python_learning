list = []

ratings = [3, 4, 6, 3, 4, 6, 5]
ratings_two = ['A', 'A', 'B', 'A', 'C', 'A']

print(ratings)
print(ratings_two)

def print_list(list):
    for item in list:
        print(item)

print_list(ratings)
print_list(ratings_two)

# first item
print(ratings[0])

# second item
print(ratings[1])

# last item
print(ratings[-1])