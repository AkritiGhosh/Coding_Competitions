# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# miniMaxSum has the following parameter(s):
# arr: an array of  integers

# Print
# Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

# Input Format
# A single line of five space-separated integers.

# Output Format
# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)


# The function accepts INTEGER_ARRAY arr as parameter.
def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[0:4]), sum(arr[1:5]))


arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
