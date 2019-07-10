dict_a = {1:1,2:2,3:3,4:4}
dict_b = {1:1,5:5,3:3,4:4}

keys_a = set(dict_a.keys())
keys_b = set(dict_b.keys())
intersection = keys_a & keys_b # '&' operator is used for set intersection
print(intersection)