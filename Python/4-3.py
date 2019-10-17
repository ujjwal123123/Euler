answer = 0

# One of i and j must be the multiple of 11 because
# a*e5 + b*e4 + c*e3 + c*e2 + b*e1 + a == 11*[9091a + 91b + 100c]
for i in range(999, 99, -1):
    for j in range(990, 99, -11):
        product = i*j
        if product > answer:
            productString = str(product)
            if productString == productString[::-1]:
                answer = product

print(answer)
