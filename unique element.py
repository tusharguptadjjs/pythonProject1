def unique(array, n):
    array.sort()
    if array[0] != array[1]:
        print(array[0], end=" ")
    for i in range(1,n-1):
        if (array[i] != array[i + 1] and array[i] != array[i - 1]):
            print(array[i], end=" ")
    if array[n - 2] != array[n - 1]:
        print(array[n - 1], end=" ")






arr=[2,2,3,4,5,2,3,4,5,1,6,7]
n=len(arr)
unique(arr,n)
