def intersect(arr1,arr2,m,n):
    i=0
    j=0
    arr2.sort()
    arr1.sort()
    while i<n and j<m:
        if arr1[i] < arr2[j]:
            i=i+1
        elif arr2[j] < arr1[i]:
            j=j+1
        else:
            print(arr1[i],end=" ")
            i=i+1
            j=j+1









arr1 = [1,2,4,2,1,7,4,2]
arr2 = [2,4,2,1,4,2,1,1]
intersect(arr1,arr2,8,8)
