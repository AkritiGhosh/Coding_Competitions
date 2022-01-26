# Comparison Sorting
# Quicksort usually has a running time of nlog(n), but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat nlog(n) (worst-case) running time, since nlog(n) represents the minimum number of comparisons needed to know where to place each element. For more details, you can see these notes (PDF).

# Alternative Sorting
# Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

# Note
# For this exercise, always return a frequency array with 100 elements.

# Returns
# int[100]: a frequency array

# Input Format
# The first line contains an integer n, the number of items in arr.
# Each of the next n lines contains an integer arr[i] where 0<i<n.

#!/bin/python3
def countingSort(arr):
    freq = [0] * 100
    for i in arr:
        freq[i] += 1
    return freq

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = countingSort(arr)

print(' '.join(map(str, result)))
print()