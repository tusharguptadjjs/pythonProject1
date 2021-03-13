def duplicate(array,n):
    array.sort()

    if n==1:
        return -1
    for i in range(n-1):
        if array[i] == array[i+1] :
            print(array[i],end=" ")
    if array[n - 2] != array[n - 1]:
        print(array[n - 1], end=" ")

arr=[2,2,3,4,5,2,3,4,5,1,6,7]
n=len(arr)
duplicate(arr,n)

