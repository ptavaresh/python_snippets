"""
Selection sort

it can sort the list in upward or downward order.

How does it work?

- It looks for the lower value into the list.
- when it founds the lower value, it swaps for the current value
- it keep looking for the lower value into the list
- and swaps it for the current one
- it will be in a loop until the index number will be iqual to the list elements


"""

array = [4,2,6,8,5,7,0]

for i in range(len(array)):
    minim = i   #store the index in i variable
    for x in range(i,len(array)): #then we walk on the list from index (i) to the end of the list
        if array[x] < array[minim]: #compare the index with the rest of the list
            minim = x # asign the min value in to the index position
    aux = array[i]
    array[i] = array[minim] #asign the value in the  index position
    array[minim] = aux
    print(array)

print('ordered list: ' + str(array))
