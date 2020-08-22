"""
Task
Given a string,S , of length N that is indexed from 0 to N-1 , print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Input Format

The first line contains an integer, T (the number of test cases).
Each line  i of the T  subsequent lines contain a String, S.
Sample Input

2
Hacker
Rank
Sample Output

Hce akr
Rn ak
"""
n=int(input())
for i in range(0, n):

    string = input()

    for j in range(0, len(string)):
        if j % 2 == 0:
            print(string[j], end='')

    print(" ", end='')

    for j in range(0, len(string)):
        if j % 2 != 0:
            print(string[j], end='')

    print("")


