# Lattice paths (Problem 15)
# ===========================

# region Problem description
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
# endregion


from math import factorial as fac

DIMENSION_X = 20
DIMENSION_Y = 20


def no_of_routes(x, y):
    return int(fac(x+y) / (fac(x)*fac(y)))


print(no_of_routes(DIMENSION_X, DIMENSION_Y))
