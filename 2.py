s = [1, 2]
sum = 0

n = 2
while s[n-1] < 4_000_000:
    s.append(s[n-1] + s[n-2])
    n += 1

m = 1
while True:
    sum += s[m]
    
    if s[m+1] > 4_000_000:
        break
    
    m += 3
    
print(sum)