'''
problem
Generate a list of 50 random values between 1 and 1000
and return multiples of 9
you'll use a list comprehension in a list comprehension
'''
import random

#my attempt
#print([x for x in [i for i in range(50) for i in range(1, 1000)] if x % 9 == 0]) # didn't get random


#correct answer
print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])