# Reciprocal cycles (Problem 26)
# ==============================

from decimal import *
getcontext().prec = 25

for i in range(1, 100):
    decimal = str(Decimal(1) / Decimal(i))[2:]

    if len(decimal) < 28:
        decimal = decimal + '0'*(30-len(decimal))

    # if decimal[0] == decimal[1] == decimal[2] == decimal[3]:
    #     print("Repetation cycle is 1 for", i)

    # if decimal[0:2] == decimal[2:4] == decimal[4:6] == decimal[6:8]:
    #     print("Repetation cycle is 2 for", i)

    # if decimal[0:3] == decimal[3:6] == decimal[6:9] == decimal[9:12]:
    #     print("Repetation cycle is 3 for", i)

    if decimal[0] == decimal[1] == decimal[2] == decimal[3]:
        print("Repetation cycle is 1 for", i)

    elif decimal[1] == decimal[2] == decimal[3] == decimal[4]:
        print("Repetation cycle is 1 for", i)

    elif decimal[0:3] == decimal[3:6] == decimal[6:9] == decimal[9:12]:
        print("Repetation cycle is 3 (case 1) for", i)

    elif decimal[1:4] == decimal[4:7] == decimal[7:10] == decimal[10:13]:
        print("Repetation cycle is 3 (case 2) for", i)

    elif decimal[2:5] == decimal[5:8] == decimal[9:11]:
        print("Repetation cycle is 3 (case 3) for", i)

    else:
        pass
