import operator

dictionary = {0: 1, 1: 3, 2: 4, 3: 1, 4: 0}
res = dict(sorted(dictionary.items(), key=operator.itemgetter(1)))
print(res)
