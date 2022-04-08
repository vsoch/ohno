#!/usr/bin/env python3

import time

# An example of a failing script

print("A first line")
time.sleep(2)
print("A second line")
time.sleep(1)
raise SystemExit("error: We cannot do that thing.")
