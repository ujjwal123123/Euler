from math import sqrt


def isPrime(n):
    for prime in primes:
        if (n % prime) == 0:
            return False
        # only check if prime is less than sqrt(n)
        if prime > sqrt(n):
            break
    return True


primes = [2, 3, ]

# Check only numbers of form 6k ± 1
i = 6
while True:
    if len(primes) == 10001:
        break
    if isPrime(i-1):
        primes.append(i-1)
    if len(primes) == 10001:
        break
    if isPrime(i+1):
        primes.append(i+1)

    i += 6

print(primes[10000])
