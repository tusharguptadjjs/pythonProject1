def equi_index(arr):
    global LS, RS, i
    n = len(arr)

    for i in range(1, n):
        LS = 0
        RS = 0
        for j in range(i):
            LS = LS + arr[j]
        for j in range(i + 1, n):
            RS = RS + arr[j]
        if LS == RS:
            return i
        else:
            return -1


arr = [-7, 1, 5, 2, -4, 3, 0]
print(equi_index(arr))
