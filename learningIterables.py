'''
iterables  is a stored sequence of values/ a list of values
in Generators they can act as an object that produces one value at a time
difference between iterable and iterators
iterable is an object with a method and returns an iterator
'''
sampStr = iter("Sample")
print("char: ", next(sampStr))
print("char: ", next(sampStr))
print("char: ", next(sampStr))