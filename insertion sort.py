def insrtsort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1], arr[j] = arr[j] ,arr[j+1]
            j=j-1
        arr[j+1]=temp


arr=[9,8,5,6,7,10]
insrtsort(arr)
print(arr)