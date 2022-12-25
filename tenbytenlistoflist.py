import random
import math

#create a 10 by 10 list
multiDlist = [[0] * 10 for i in range(10)]
multiDlist[0][1] = 10
print(multiDlist[0][1])

listTable =  [[0] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        listTable[i][j] = "{} : {}" .format (i, j)
for i in range(4):
    for j in range(4):
        print(listTable[i][j], end = "||")
    print()