# 1000-digit Fibonacci number (Problem 25)
# ========================================

# region Description
# The Fibonacci sequence is defined by the recurrence relation:

#     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

# Hence the first 12 terms will be:

#     F1 = 1
#     F2 = 1
#     F3 = 2
#     F4 = 3
#     F5 = 5
#     F6 = 8
#     F7 = 13
#     F8 = 21
#     F9 = 34
#     F10 = 55
#     F11 = 89
#     F12 = 144

# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
# endregion

fibonacciList = {1: 1, 2: 1}


def fibonacci(n):
    if n not in fibonacciList:
        fibonacciList[n] = fibonacciList[n-1] + fibonacciList[n-2]

    return fibonacciList[n]


def main():
    n = 1
    while True:
        if len(str(fibonacci(n))) >= 10000:
            print(n)
            break

        n += 1


if __name__ == "__main__":
    main()
