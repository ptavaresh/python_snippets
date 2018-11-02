
lst = [1,2,3,4,5,6,7]
lst.reverse() # it modifies the original list
print(lst)

lst = [1,2,3,4,5,6,7]
lst[::-1] #this create a copy of the list and doesn't modify the original list
print(lst[::-1])

lst = [1,2,3,4,5,6,7]
print(list(reversed(lst))) # it doesn't modify the original list instead of that it point to the index
newlist = list(reversed(lst) # we can create a new list object in a new variable
print(newlist)
