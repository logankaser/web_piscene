#!/usr/bin/env python3

import sys, re

args = sys.argv[1:]
args = (" ".join(args))
args =  re.sub(" +"," ", args)
print("\n".join(sorted(args.split())))
