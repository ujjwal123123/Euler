n = 1000

# 31875000
# 4 function calls in 0.196 seconds
#########################################
for a in range(1, n):
    b = a+1
    while a + b < n:
        if a**2 + b**2 == (n - a - b)**2:
            print(a*b*(n-a-b))
        b += 1
