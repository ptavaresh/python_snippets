def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]
gen_expr = (x * x for x in range(3))

print_vector(*gen_expr) # unpacking a list or tuple 

dict_vector = {'x': 1, 'y': 0, 'z':1} # unpacking a dictionary as an argument for a function
print_vector(**dict_vector)
