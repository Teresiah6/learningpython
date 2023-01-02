'''
generator function is going to return a result generator whenever you call it
and you are going to be able to resume during execution of your prog
 to create results over time over time rather than at once
 ordinarily used to generate a very large result set
 and don't wnat to slow donw the program by creating results at once
'''
def isPrime(num):
    for i in range(2, num):
        if num % i  == 0:
            return False
    return True
def gen_prime(max_number):
    for num1 in range(2, max_number):
        if isPrime(num1):
            yield num1
prime = gen_prime(50)
print("prime: ", next(prime))
print("prime: ", next(prime))
print("prime: ", next(prime))
print("prime: ", next(prime))
print("prime: ", next(prime))
