#!/usr/bin/env python3

def representsInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

while True:
    try:
        s = input("Enter a number: ")
        if representsInt(s):
            print("The number {} is {}".format(s, "even" if int(s) % 2 == 0 else "odd"))
        else:
            print("'{}' is not a number".format(s))
    except (EOFError, KeyboardInterrupt):
        break
