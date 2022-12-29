'''
reduce receives a list and returns a single result - is imported
'''
from functools import reduce
#add up the values in a list
print(reduce((lambda x,y: x+y), range(1, 6)))