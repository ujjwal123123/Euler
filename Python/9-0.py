import math

n = 1000

# 31875000.0
# 997067 function calls in 0.410 seconds
##########################################
for a in range(1, n):
    for b in range(a+1, n):
        c = math.sqrt(a**2 + b**2)
        if c == math.floor(c):
            if a + b + c == n:
                print(a*b*c)
