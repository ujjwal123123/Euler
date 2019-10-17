answer = 0

for i in range(0, 1000):
    for j in range(0, 1000):
        if str(i*j) == str(i*j)[::-1] and i*j >= answer:
            answer = i*j

print(answer)
