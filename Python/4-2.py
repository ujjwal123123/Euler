answer = 0

# One of i and j must be the multiple of 11 because
# a*e5 + b*e4 + c*e3 + c*e2 + b*e1 + a == 11*[9091a + 91b + 100c]
for i in range(999, 100, -1):
    for j in range(990, 100, -11):
        product = i*j
        if str(product) == str(product)[::-1] and product > answer:
            answer = product

print(answer)
