def mergesortedarr(array1, arr2):
    length = len(array1)
    length2 = len(arr2)
    arr = []
    i = 0
    j = 0
    while (i < length) and (j < length2):
        if array1[i] < arr2[j]:
            arr.append(array1[i])
            i = i + 1
        else:
            arr.append(arr2[j])
            j = j + 1
    while i < length:
        arr.append(array1[i])
        i = i + 1
    while j < length2:
        arr.append(arr2[j])
        j = j + 1
    return arr


arr1 = [1, 4, 9, 10]
arr2 = [2, 3, 6, 7, 8]
print(mergesortedarr(arr1, arr2))
