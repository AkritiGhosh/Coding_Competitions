# Sean invented a game involving a 2n*2n matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum of the elements in the n*n submatrix located in the upper-left quadrant of the matrix.

# Given the initial configurations for q matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.


# Input Format
## The first line contains an integer q, the number of queries.
## The next q sets of lines are in the following format:
## The first line of each query contains an integer, n.
## Each of the next 2n lines contains 2n space-separated integers matrix[i][j] in row i of the matrix.

#!/bin/python3

import math
import os
import random
import re
import sys


def flippingMatrix(n, a):
    # Write your code here
    max_val = 0
    for i in range(n):
        for j in range(n):
            max_val += max([a[i][j],a[2*n-i-1][j],a[i][2*n-j-1],a[2*n-i-1][2*n-j-1]])
    return max_val

q = int(input().strip())
for q_itr in range(q):
    n = int(input().strip())
    matrix = []
    for _ in range(2 * n):
        matrix.append(list(map(int, input().rstrip().split())))
    result = flippingMatrix(n, matrix)
    print(result)