#!/usr/bin/python3

def print_last_digit(number):
    last_digit = abs(number) % 10  # abs convert number negative/positive
    print(last_digit, end="")

    return last_digit
