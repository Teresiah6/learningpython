#tuples are like lists but values cannot be changed inside of a list
myTuple = (1,2,3,5,8)
print("1st value: ", myTuple[0])
#slicing tuples
print(myTuple[0:3])
print("Tuple Length: ", len(myTuple))
#concatenate myTuple
morefibs = myTuple + (13, 21, 34)
#check values in tuple, returns true or false
print("32 in Tuple: ", 34 in morefibs)
for i in morefibs:
    print(i)
#convert a list into a tuple
aList = [55, 89, 144]
aTuple = tuple(aList)
#convert a tuple to a list
alist = list(aTuple)
#getting maximum and mimn value ina tuple
print("Min: ", min(aTuple))
print("Max: ", max(aTuple))
