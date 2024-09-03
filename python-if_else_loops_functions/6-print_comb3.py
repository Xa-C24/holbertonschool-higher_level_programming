#!/usr/bin/python3
for number in range(0, 10):
    for next_number in range(number + 1, 10):
        print(f"{number}{next_number}", end="")
        if number == 8 and next_number == 9:
            print()
        else:
            print(", ", end="")
