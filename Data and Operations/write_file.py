# open a file for writing
# f = open("test.txt", "w")

# append to a file, this will add text to the end of it
f = open("text.txt", "a")

# write data to file
f.write("Hello World, \n")
f.write("This data will be written to the file.")
f.close()

f = open("text.txt", "a")
f.write("Don't delete existing data \n")
f.write("Add this to the existing file")
f.close()