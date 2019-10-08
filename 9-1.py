import math

n = 1000

# 31875000.0
# 249067 function calls in 0.202 seconds
##########################################
for a in range(1, n):
    b = a+1
    while a + b < n:
        c = math.sqrt(a**2 + b**2)
        if a + b + c == n:
            if c == math.floor(c):
                print(a*b*c)
        b += 1
