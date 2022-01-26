# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# Return
# int: the absolute diagonal difference

# Input Format
# The first line contains a single integer, n, the number of rows and columns in the square matrix arr.
# Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].

# Output Format
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

# #!/bin/python3

def diagonalDifference(arr):
    n = len(arr)
    fd_sum = 0
    bd_sum = 0
    for i in range(n):
        fd_sum += arr[i][i]
        bd_sum += arr[i][n-i-1]
    return abs(fd_sum-bd_sum)

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(arr)
print(result)