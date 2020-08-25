#!/bin/python3

import sys


S = input().strip()
try:
    change = int(S)
    print(change)
except:
    print("Bad String")
    