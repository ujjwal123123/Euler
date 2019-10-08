x,y,sigma = 1,2,0

while y <= 40_00_000:
    sigma += y
    x, y = x + 2*y, 2*x + 3*y

print(sigma)