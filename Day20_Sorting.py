#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps=0
for i in range(n):
    for num in range(0,n-1):
        if a[num] > a[num+1]:
            a[num],a[num+1] = a[num+1],a[num]
            numSwaps+=1
        
print("Array is sorted in {} swaps.".format(numSwaps))
print("First Element:",a[0])
print("Last Element:",a[-1])

