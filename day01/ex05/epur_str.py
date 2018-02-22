#!/usr/bin/env python3

import sys, re

if sys.argv[1]:
    print(re.sub(" +"," ", sys.argv[1].strip()))
