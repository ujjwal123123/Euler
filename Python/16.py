
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?

NUMBER = 2**1000

def sum_of_digits(n):
    '''
    Returns sum of digits in a number.
    n: number (type must be int)
    '''

    sum = 0
    
    number = str(NUMBER)

    for i in number:
        sum += int(i)

    return sum

print(sum_of_digits(NUMBER))