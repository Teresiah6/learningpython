import math
import random

numlist = []
for i in range(5):
    numlist.append(random.randrange(1, 10))
#sorting
numlist.sort()
#reverse sort
numlist.reverse()
#insert at index 5 which is at the end, num 10
numlist.insert(5, 10)
#remove an item in a list
numlist.remove(10)
#remove an item at a acertain index
numlist.pop(2)

for k in numlist:
    print(k, end=", ")
print()