#!/usr/bin/env python3

def representsInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
