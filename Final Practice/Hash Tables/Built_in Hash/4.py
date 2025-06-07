# hash() method used by one immutable object, if we use this on a mutable object like list, set, dictionaries then it will generate an error.
l = [1, 2, 3, 4]
print(hash(l))
