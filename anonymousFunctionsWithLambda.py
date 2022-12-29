"""
Lmbda is very similar to def
But rather than allowing you to assign a function to a name
lambda is simply going returning
Because there is no name that is why they are also known as anonymous functions
Example: lambda arg1, arg2, ........: expression use the args
used when you need a small function but don't want to have a lot of function names
 that may cause various issues
"""
import random
sum = lambda x, y: x+y
print("Sum: ", sum(4,5))

#ternary operator to see  if someone can vote
can_vote = lambda age: True if age >=18 else False
print("can Vote: ", can_vote(19))

#create a list of functions
powerList = [lambda x: x**2,
             lambda x: x**3,
             lambda x: x**4]

# learn the different fucntions against one value
for func in powerList:
    print(func(4))

#storing lambdas inside of dictionaries
attack = {'quick': (lambda: print('Quick Attack')),
          'power': (lambda: print('Power Attack')),
          'miss': (lambda: print('Missed Attack'))}
attack['quick']()

attackKey = random.choice(list(attack.keys()))

attack[attackKey]()

