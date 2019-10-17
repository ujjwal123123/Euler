# Names scores (Problem 22)
# =========================

# region Description
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?
# endregion

file = open('p022_names.txt', 'r')

names = []


def loadName(file, names):
    '''
    Read names from file into an array

    file: file which has names in it
    names: an array
    '''

    for line in file:
        insideQuote = False
        for char in line:
            if 
            


def nameScore(name):
    score = 0

    for char in name:
        score += ord(char) - ord('A') + 1

    return score
