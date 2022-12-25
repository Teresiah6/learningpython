import random
import math
#generate a random list
numList = []
#5 numbers between 1 and 9
for i in range (5):
    numList.append(random.randrange(1, 10))

for i in numList:
    print(i)