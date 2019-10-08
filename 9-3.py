n = 1000

# Using perimeterisation
for y in range(1,n):
    x = y
    while 2*x*(x+y) <= n:
        if 2*x*(x+y) == n:
            print(n*(x-y)*y*(x**2 + y**2))
        x += 1