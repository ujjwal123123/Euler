import math


def largestPrimeFactors(n):
    for i in possiblePrimeFactors(n)[::-1]:
        if isPrime(i) == True:
            return i


def possiblePrimeFactors(n):
    factors = []
    if n % 2 == 0:
        factors.append(2)
    if n % 3 == 0:
        factors.append(3)

    i = 5
    while i*i <= n:
        if n % i == 0:
            factors.append(i)
        if n % (i+2) == 0:
            factors.append(i+2)
        i += 6

    return factors


def isPrime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    # Only check numbers of form 6k+1 or 6k-1
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


print(largestPrimeFactors(600851475143))
