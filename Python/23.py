# First we need to find numbers which cannot be written as sum of abundant numbers
from math import sqrt


def sum_divisors(n):
    sum = 0

    for i in range(1,n):
        if (n % i == 0):
            sum += i

    return sum

