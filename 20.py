# Factorial digit sum (Problem 20)
# ================================

# region Problem Description
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!
# endregion

from math import factorial


n = factorial(100)

s = str(n)

sum = 0

for i in s:
    sum += int(i)

print(sum)
