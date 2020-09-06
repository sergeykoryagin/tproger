dict_1 = {1: 2, 2: 3, 4: 5, 5: 6}
dict_2 = {6: 1, 7: 5, 8: 8}
dict_3 = {9: 4, 10: 10, 11: 12}
res = {}

for dictionary in (dict_1, dict_2, dict_3):
    res.update(dictionary.items())

print(res)