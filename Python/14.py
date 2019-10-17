# Longest Collatz sequence
# ========================
# NOTE: needs optimaization:
#   * caching
#   * see pdf also

# region Problem description
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?
# endregion


num = 0
maxLen = 0
lenList = []


def collatzLen(n, length=1):
    """
    Return length of collatz sequence for number n

    n: a natural number
    Returns: length of Collatz sequence
    """
    if n == 1:
        return(length)
    # even
    elif n % 2 == 0:
        return collatzLen(int(n/2), length + 1)
    # odd
    else:
        return collatzLen(3*n + 1, length + 1)

    lenList.append((n, length))


for n in range(1_000_000, 1, -1):

    if collatzLen(n) > maxLen:
        num = n

        maxLen = collatzLen(n)
        print(num, maxLen)
