#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    total = 0
for arg in argv:
    total += int(arg)
print(total)
