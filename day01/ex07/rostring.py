#!/usr/bin/env python3

import sys

if len(sys.argv) >= 2:
    arg = sys.argv[1].split()
    tmp = arg[0]
    arg[0] = arg[-1]
    arg[-1] = tmp
    print(" ".join(arg))
