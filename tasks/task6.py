number = input("Введите число:")
while True:
    notation = int(input("Введите его систему счисления(от 2 до 36):"))
    if 1 < notation < 37:
        break
    else:
        print("от 2 до 36!")
res = int(number, notation)
print("Введенное число в десятичной системе счисления:", res)