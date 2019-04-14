"""
Bubble sort

checks every element of the list and compares withe the next element,
if the first element is higher than the second element,
it exchange the order of the elements.

e.g.

4   2   6   8   5   7
2   4   6   8   5   7
2   4   6   5   8   7
2   4   6   5   7   8
2   4   5   6   7   8

"""

array = [4,2,6,8,5,7]

for i in range(len(array)):
    for x in range(len(array)-1):
        if array[x] > array[x+1]:
            aux =array[x]
            array[x] = array[x+1]
            array[x+1] = aux
            print(array)
            print('iteration: ' + str(i))
