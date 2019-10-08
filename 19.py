# Counting Sundays (Problem 19)
# =============================

# region Problem Description
# You are given the following information, but you may prefer to do some research for yourself.

# * 1 Jan 1900 was a Monday.

# * Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.

# * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# endregion

day = 2

sundays = 0


def isLeap(year):
    '''
    Return if an year is leap or not
    '''
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def daysIn(month, year):
    '''
    Returns number of days in a month
    '''

    # January
    if month == 0:
        return 31

    # February
    elif month == 1:
        if isLeap(year):
            return 29
        else:
            return 28

    # March
    elif month == 2:
        return 31

    # April
    elif month == 3:
        return 30

    # May
    elif month == 4:
        return 31

    # June
    elif month == 5:
        return 30

    # July
    elif month == 6:
        return 31

    # August
    elif month == 7:
        return 31

    # September
    elif month == 8:
        return 30

    # October
    elif month == 9:
        return 31

    # November
    elif month == 10:
        return 30

    # December
    elif month == 11:
        return 31

    else:
        raise Exception(
            "days function was provided incorrect input. Input must be between 0 and 11 (inclusive)")


for year in range(1901, 2001):
    for month in range(12):
        if day % 7 == 0:
            sundays += 1
            print('1 of', month, year, 'was sunday')

        day += daysIn(month, year)

print(sundays)
