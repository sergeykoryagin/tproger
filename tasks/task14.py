def even_nums(lst):
    for num in lst:
        if num == 237:
            return
        elif num % 2 == 0:
            print(num)


lst = [1, 23, 14, 1241, 1512, 16, 17, 1532, 237, 141, 14, 16, 18, ]

even_nums(lst)
