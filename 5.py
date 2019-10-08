n = 2520

for i in range(11, 21):
    while True:
        if n % i == 0:
            break
        n += 1

print(n)