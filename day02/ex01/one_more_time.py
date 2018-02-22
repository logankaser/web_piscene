#!/usr/bin/env python3

from datetime import datetime
import sys, locale

locale.setlocale(locale.LC_ALL,'fr_FR')

if len(sys.argv) == 2:
    try:
        print(int(datetime.strptime(sys.argv[1], "%A %d %B %Y %X").timestamp()))
    except ValueError:
        print("Wrong Format")
