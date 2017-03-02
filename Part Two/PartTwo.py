from math import sqrt

def is_prime(num):
    #2 and 3 are automatically primes
    if num == 2 or num == 3:
        return True
    #anything below 2 or any even number are automatically not primes
    elif num < 2 or num % 2 == 0:
        return False
    #anything that passes the above statement and is less than 9 is a prime
    elif num < 9:
        return True
    #any multiple of 3 is not a prime
    elif num % 3 == 0:
        return False
    r = sqrt(num)
    f = 5
    while f <= r:
        if num % f == 0 or num % (f + 2) == 0:
            return False
        else:
            f += 6
    return True

#generator function to get primes from argument to infinity
def get_primes(c):
    while(True):
        if is_prime(c):
            yield c
        c += 1

#gets sum of all primes from argument up to 2 million
def sum_primes(x):
    getPrime = get_primes(x)
    sum = 0
    while(True):
        temp = next(getPrime)
        if temp > 2000000:
            print("Problem 10 of Project Euler complete. Answer: " + str(sum))
            break
        else:
            sum = sum + temp
            #print(sum) for testing purposes

x = int(input("What number would you like to start from?\n"))
print("Please wait while I calculate the answer. This make take a few seconds.\n")
sum_primes(x)
