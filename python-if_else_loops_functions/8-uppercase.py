#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord(c) >= 97 and ord(c) <= 122:
            char = chr(ord(char) - 32)
            print("{s}".format(char), end="")
    print()
