# pickle can serialize and deserialize objects
# serialized objects can be saved and loaded from the disk
# pickling is converting an object (list, dict, etc) to a file and vice versa

# Idea is to save one or more objects in one script and load them in another. Can be used to save program or game states

import pickle

exampleObj = {'Python':3,'KDE':5,'Windows':10}

# serialize object
fileObj = open("data.obj", "wb")
pickle.dump(exampleObj, fileObj)
fileObj.close()

# deserialize object
# now that it's been saved, can load it (unpickle it)

fileObj = open("data.obj", "rb")
exampleObj = pickle.load(fileObj)
fileObj.close()
print(exampleObj)

