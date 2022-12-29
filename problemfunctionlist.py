'''
Create a function that receives a list and a function
The function passed will return True or False if a last value is odd
The surrounding functions will return a list of odd numbers
'''
def isItOdd(num):
    if not num % 2 == 0:
        return num
def change_list(list,func):
    oddList = []
    for i in list:
        if func(i):
            oddList.append(i)
    return oddList
aList = range(1, 20)

print(change_list(aList, isItOdd))