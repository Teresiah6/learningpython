'''
#list comprehensions in list comprehensions
# Generete  a list of 10 values
multiply them by 2
return mltiples of 8
'''
print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])