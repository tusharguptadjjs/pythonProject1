def selectionsort(arr):
    for i in range(len(arr)-1):
        mi=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[mi]:
                mi=j
                arr[mi] , arr[i] = arr[i] , arr[mi]
arr = [1,5,3,7,2,6,0]
selectionsort(arr)
print(arr)
                