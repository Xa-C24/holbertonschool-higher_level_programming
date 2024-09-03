#!/usr/bin/python3
for number in range(0, 10):
    for next_number in range(number + 1, 10):
        if number == 8 and next_number == 9:
            print("{}{}".format(number, next_number))
        else:
            print("{}{}, ".format(number, next_number), end="")
