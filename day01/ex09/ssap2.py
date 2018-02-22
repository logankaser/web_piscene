#!/usr/bin/env python3

import sys, re, string

args = sys.argv[1:]
args = (" ".join(args))
args = re.sub(" +"," ", args)
mixed = sorted(args.split(), key=str.lower)

alpha = list(filter(lambda x: str(x[0]).isalpha(), mixed))
num = list(filter(lambda x: str(x[0]).isdigit(), mixed))
special_chars = set(string.punctuation)
special = list(filter(lambda x: x[0] in special_chars, mixed))
if len(alpha):
    print("\n".join(alpha))
if len(num):
    print("\n".join(num))
if len(special):
    print("\n".join(special))
