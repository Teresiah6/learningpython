#a function that takes in multiple arguments
def sumAll(*args):
    sum = 0

    for i in args:
        sum += i

    return sum
print("Sum: ", sumAll(1,2,3,4,5))

def multAll(*args):
    mult =1;

    for i in args:
        mult *= i
    return mult

print("Product: ", multAll(1,2,3,4,5))

