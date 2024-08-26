number = ''
def biggest_odd(number):
    maximum = 0
    for num in number:
       if int (number) > maximum and int (number) % 2 == 1:
            maximum = number
    return maximum



