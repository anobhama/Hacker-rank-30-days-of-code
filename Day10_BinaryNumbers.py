"""
Task
Given a base- integer,10 ,n convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

Input Format

A single integer, n.
Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
"""
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    result = 0
    count = 0

    while n > 0:
        if n % 2 == 1:
            result += 1
            if result > count:
                count = result

        else:
            result = 0
        n //= 2
    print(count)
