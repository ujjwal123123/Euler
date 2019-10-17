from math import sqrt

NUMBER_OF_DIVISORS = 500


def main():
    i = 1
    while True:
        if no_of_divisors(triangle_number(i)) >= NUMBER_OF_DIVISORS:
            print(triangle_number(i))
            break
        i += 1


def no_of_divisors(n):
    '''
    Return number of divisors for a given number.
    '''

    number = 0

    # Check from 1 to sqrt(n) for divisors
    for i in range(1, int(sqrt(n))):
        if n % i == 0:
            number += 1

    # Include divisors like n/previously considered divisors
    number *= 2

    # Check if n is perfect square
    if n % int(sqrt(n)) == 0:
        number += 1

    return number


def triangle_number(n):
    '''
    Return n th triangle number
    '''
    return int((n * (n+1))/2)


if __name__ == "__main__":
    main()
