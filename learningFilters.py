#filter selects items from a list based of a function
#print out the even values from a list
print(list(filter((lambda x: x % 2 == 0), range(1,11))))
