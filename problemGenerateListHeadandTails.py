'''
create a random list filled with characters H and T
for heads and tails. Output the number of Hs and Ts
example output
Heads: 46
Tails: 54
'''
import random

#create the list
flipList = []
# populate with 100 H's and T's
for i in range(1,101):
    flipList += random.choice(['H', 'T'])

# output the results
print("Heads: ", flipList.count('H'))
print("Heads: ", flipList.count('T'))