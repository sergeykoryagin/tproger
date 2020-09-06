def unique(lst):
    return len(lst) == len(set(lst))


lst1 = [1, 2, 3, 4, 5, 6, 7]
lst2 = [1, 2, 3, 4, 3, 2, 1]

print(unique(lst1))
print(unique(lst2))
