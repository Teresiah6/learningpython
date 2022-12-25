#fibonaci numbers
#1, 1, 2, 3, 5, 8, 13..
#create using recurssive function
#fn = Fn -1 + Fn -2
#get out of recurssion if F0 = 0 F1 = 1
#print (fib3)
#1 = fib(2) +fib(1)
#2nd: = fib(1) + (fib(0)) + fib(0)
def fib(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        result = fib(num-1) + fib(num -2)
        return result

print(fib(3))
print(fib(4))
print(fib(5))

#listing a certain number of fibonaci numbers
#ask how man numbers
numFibVals = int(input("How many fibonacci values do you want: "))
# loop calling each new num
i = 1
while i < numFibVals:
    fibValue = fib(i)
    print(fibValue)
    i+= 1

print("ALL DONE")