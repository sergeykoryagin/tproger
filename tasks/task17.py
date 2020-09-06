def sum_of_digits(number):
    sum = 0
    for digit in number:
        sum += int(digit)
    return sum


number = input()

print(sum_of_digits(number))
