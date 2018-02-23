#!/usr/bin/env python3

import users
from datetime import datetime

lst = users.users()
for u in lst:
    time = datetime.fromtimestamp(u[3]).strftime("%b %d %H:%M")
    print("{}   {}  {}".format(u[0], u[1], time))

