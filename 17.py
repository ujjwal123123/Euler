# Number letter counts (Problem 17)
# =================================

# region Problem description
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
# endregion


answer = 0


def count(number):
    if number == '0':
        return 0
    elif number == '1':
        return len('one')
    elif number == '2':
        return len('two')
    elif number == '3':
        return len('three')
    elif number == '4':
        return len('four')
    elif number == '5':
        return len('five')
    elif number == '6':
        return len('six')
    elif number == '7':
        return len('seven')
    elif number == '8':
        return len('eight')
    elif number == '9':
        return len('nine')


def length(i):
    '''
    Return no of letters
    '''
    no_of_letter = 0

    if str(i) == '1000':
        no_of_letter += len('onethousand')

    elif len(str(i)) >= 3:
        no_of_letter += count(str(i)[-3])
        no_of_letter += len('hundred')
        no_of_letter += len('and')

    if len(str(i)) >= 2:
        tens_place = str(i)[-2]
        ones_place = str(i)[-1]

        if tens_place == '1':
            if ones_place == '0':
                no_of_letter += len('twenty')
            elif ones_place == '1':
                no_of_letter += len('eleven')
            elif ones_place == '2':
                no_of_letter += len('twelve')
            elif ones_place == '3':
                no_of_letter += len('thirteen')
            elif ones_place == '4':
                no_of_letter += len('fourteen')
            elif ones_place == '5':
                no_of_letter += len('fifteen')
            elif ones_place == '6':
                no_of_letter += len('sixteen')
            elif ones_place == '7':
                no_of_letter += len('seventeen')
            elif ones_place == '8':
                no_of_letter += len('eighteen')
            elif ones_place == '9':
                no_of_letter += len('nineteen')
        elif tens_place == '2':
            no_of_letter += len('twenty')
            no_of_letter += count(ones_place)
        elif tens_place == '3':
            no_of_letter += len('thirty')
            no_of_letter += count(ones_place)
        elif tens_place == '4':
            no_of_letter += len('fourty')
            no_of_letter += count(ones_place)
        elif tens_place == '5':
            no_of_letter += len('fifty')
            no_of_letter += count(ones_place)
        elif tens_place == '6':
            no_of_letter += len('sixty')
            no_of_letter += count(ones_place)
        elif tens_place == '7':
            no_of_letter += len('seventy')
            no_of_letter += count(ones_place)
        elif tens_place == '8':
            no_of_letter += len('eighty')
            no_of_letter += count(ones_place)
        elif tens_place == '9':
            no_of_letter += len('ninety')
            no_of_letter += count(ones_place)

    if len(str(i)) == 1:
        ones_place = str(i)[-1]
        no_of_letter += count(ones_place)

    return no_of_letter


for i in range(1, 1000):
    answer += length(i)

print(answer)
