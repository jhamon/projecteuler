ns = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    '100': 'hundred',
    '1000': 'one thousand'}


def n2s(n):
    return ns[str(n)]


def printXX():
    totalstr = ''
    for i in range(1, 100):
        if i < 21:
            totalstr = totalstr + n2s(i)
            # print i, n2s(i)
        elif i % 10 == 0:
            totalstr = totalstr + n2s(i)
            # print i, n2s(i)
        else:
            totalstr = totalstr + n2s(i - i % 10) + n2s(i % 10)
            # print i, n2s(i-i%10)+n2s(i%10)
    return len(list(totalstr))

zero2ninetynine = printXX()


def hundreds():
    hundredsstr = ''
    for i in range(100, 1000, 100):
        # print i, n2s(i/100)+n2s(100)
        hundredsstr = hundredsstr + n2s(i / 100) + n2s(100)
    return len(list(hundredsstr))

hundredsstr = hundreds()
ands = len(range(1, 100)) * 3
print 9 * ands + 100 * hundredsstr + zero2ninetynine * 10 + len(list(
    'onethousand'))
