inpfile = open("13.txt", "r")

sum = 0

for line in inpfile:
    # calculate sum of only first 11 digits
    sum += int(line[0:11])

inpfile.close()
# print first 10 digits of the sum
print(str(sum)[0:10])