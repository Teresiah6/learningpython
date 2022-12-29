'''
Find the multiples of 9 from a random 100 value list with
values between 1 and 10
'''
import random
alist = list(random.randint(1, 1000) for i in range (100))
#use range to generate 100 values
print(list(filter((lambda x: x % 9 == 0), alist)))