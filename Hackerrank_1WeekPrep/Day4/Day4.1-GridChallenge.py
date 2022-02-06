#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    for i in range(len(grid)):
        grid[i]=  sorted(grid[i])
    grid =[[row[i] for row in grid] for i in range(len(grid[0]))]
    gc = list(grid)
    
    same = True
    for i in range(len(gc)):
        gc[i]=  sorted(gc[i])
        if gc[i] !=grid[i]:
            return 'NO'
    return 'YES'

t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = gridChallenge(grid)

print(result)
