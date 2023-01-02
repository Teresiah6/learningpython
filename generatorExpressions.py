'''
generator expressions look just like list comprehensions
but return results one at a time
surrounded by parenthesis instead of []
'''
double = (x * 2 for x in range (10))
print("Double: ", next(double))
print("Double: ", next(double))

# iterating through the results
for num in double:
    print(num)