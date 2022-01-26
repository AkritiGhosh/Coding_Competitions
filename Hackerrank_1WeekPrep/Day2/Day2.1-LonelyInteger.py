# Given an array of integers, where all elements but one occur twice, find the unique element.

# Returns
# int: the element that occurs only once

# Input Format
# The first line contains a single integer, n, the number of integers in the array.
# The second line contains n space-separated integers that describe the values in a[].

#!/bin/python3

def lonelyinteger(a):
    done = False
    idx = 0
    # Write your code here
    a.sort()
    while done == False:
        if len(a) == 1:
            return a[0]
        if len(a) == 2 and a[0] != a[1]:
            return a[0]
        if a[1] == a[0]:
            a.remove(a[1])
            a.remove(a[0])
        else:
            return a[0]

n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = lonelyinteger(a)
print(result)