from math import sqrt

sum = 5
primes = [2, 3, ]

def isPrime(n):
    for prime in primes:
        if (n % prime) == 0:
            return False
        # only check if prime is less than sqrt(n)
        if prime > sqrt(n):
            break
    return True

n = 6
while n < 2_000_000:
    if n >= 2_000_000:
        break
    if isPrime(n-1):
        primes.append(n-1)
        sum += n-1
    if n >= 2_000_000:
        break
    if isPrime(n+1):
        primes.append(n+1)
        sum += n+1

    n += 6

print(sum) 