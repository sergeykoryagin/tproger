def difference(lst1, lst2):
    lst3 = []
    for elem in lst1:
        if elem not in lst2:
            lst3.append(elem)
    return lst3


lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = [2, 4, 6, 8]

print(difference(lst1, lst2))
