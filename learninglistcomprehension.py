'''
a list comprehension executes an expression against an iterable
like is done in map and filter
make sure not to complicate them for others or your future self
'''
print(list(map((lambda x: x * 2), range(1, 11))))
# the list comprehension
print([2 * y for y in range(1, 11)])
#comparison of list comprehension to filter
print(list(filter((lambda x: x % 2 != 0), range(1, 11))))
#list comprehnsion
print([x for x in range(1, 11) if x % 2 != 0])
#list comprehension that can act like a map and fil;ter on one line
#generate a list of 50 values and take them to the power of 2 and retun all multiples of 8
print([i ** 2 for i in range(50) if i % 8 == 0])
#list comprehensions also allow for multiple for loops
# multiply  all values in one list by all values in another list
print([x * y for x in range(1, 3) for y in range(11, 16)])


