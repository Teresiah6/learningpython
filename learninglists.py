import random
import math

#list
#[0 : "string"] [1: 1234] [2: 28] [3 : "c"]
randList = ["string", 1.234, 28]
#list using range
oneToTen = list(range(10))
#concatenate lists
randList = randList + oneToTen
print(randList[0])
print("List length: ", len(randList))

first3 = randList[0:3]
for i in first3:
    print(f"{first3.index(i)}: {i}")

#print an item on a list three times
print(first3[0] * 3)
print("string" in first3)
#find index of a word
print("Index of string: ", first3.index("string"))
#how many times an item is contained in a list
print("How many strings: ", first3.count("string"))
print("How many 1's ", first3.count("string"))
#changing the string
first3[0] = "new string"
for i in first3:
    print(f"{first3.index(i)}: {i}")
#add an item into the list
first3.append("Another")
for i in first3:
    print(f"{first3.index(i)}: {i}")
