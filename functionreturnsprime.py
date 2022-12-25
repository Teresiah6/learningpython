#A prime is divisible by itself and 1
#e.g 5
#input max prime to search
#use a loop and check if modulus  == 0 True
def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True


#print the list of primes
def getprimes(max_num):
    list_of_primes = []
    for num1 in range(2, max_num):
        if isPrime(num1):
            list_of_primes.append(num1)

    return list_of_primes

max_num_to_check = int(input("Search for prime numbers upto: "))
list_of_primes = getprimes((max_num_to_check))
for prime in list_of_primes:
    print(prime)