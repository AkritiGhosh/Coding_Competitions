# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Print
# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 6 digits after the decimal. The function should not return a value.

# # Input Format
# The first line contains an integer, n, the size of the array.
# The second line contains n space-separated integers that describe arr[n].

# # Output Format
# Print the following 3 lines, each to 6 decimals:
# 1.proportion of positive values
# 2.proportion of negative values
# 3.proportion of zeros

# #!/bin/python3

def plusMinus(m,arr):
    positive_count = 0
    negative_count = 0
    zero = 0

    for n in arr:
        if n < 0:
            negative_count += 1
        elif n > 0 : 
            positive_count += 1
        else:
            zero += 1
    print("{:.6f}".format(positive_count/m))
    print("{:.6f}".format(negative_count/m))
    print("{:.6f}".format(zero/m))
    

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

plusMinus(n,arr)
