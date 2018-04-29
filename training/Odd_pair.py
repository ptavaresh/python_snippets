"""
Provide a rank of numbers and get the Odd and Pairs.
"""
l = 18
r = 10

def oddPair(l, r):
    for l in range(l,r):
        isOdd = l % 2
        if isOdd is not 0:
            print('Odd: ' + str(l))
        else:
            print('Pair: ' + str(l))

if int(l) < int(r):
    oddPair(l,r)

elif int(l) == int(r):
    print('Values are iqual.')

elif int(l) > int(r):
    print('First value is higher than the second one, however we swap them for you!!!')
    oddPair(r,l)
