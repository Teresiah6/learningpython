# a recursive function is one that refers itself
#calls itself inside of itself
#calculate factorials
#factorial of 3 = 3 * 2 * 1
def factorial(num):
    #condition for when factorial shouldn't call itsef
    if num <= 1:
        return  1
    else:
        result = num * factorial(num - 1)
        return result
print("4! = ",factorial(4))