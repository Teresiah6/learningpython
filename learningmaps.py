"""
allows us to execute a function on each item in a list
"""
#generate a list
oneToTen = range(1, 11)
#function to pass into the map function
def dbl_num(num):
    return num * 2
print(list(map(dbl_num, oneToTen)))

#with lambda
print(list(map((lambda x: x * 3), oneToTen)))

#perform calculations against multiple different lists
aList = list(map((lambda x,y: x+y), [1, 2, 3], [1,2,3]))
print(aList)

anotherList = list(map((lambda x, y: x+y), [2, 4, 6], [1,2,3]))
print(anotherList)

