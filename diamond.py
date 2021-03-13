def largestarray(arr):
    l= arr[0]
    for i in range(len(arr)):
        if arr[i] > l:
            l = arr[i]
    return l

arr = [2,3,4,44,6,7]
array = largestarray(arr)
print(array)
