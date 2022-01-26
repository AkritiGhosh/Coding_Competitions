# Given an array of numbers, find the median value
#!/bin/python3

def findMedian(arr):
    i=0
    arr.sort()
    print(arr)
    if len(arr)%2 != 0: 
    # Even no of elements
        return arr[len(arr)//2]
    else:
        i = arr[len(arr)//2] + arr[(len(arr)-1)//2]
        return i/2

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = findMedian(arr)
print(result)