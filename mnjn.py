def arrayEquilibriumIndex(arr, n):
    LS, RS = 0, 0
    for i in range(n):
        RS = RS + arr[i]
    for i in range(n):
        RS = RS - arr[i]
        if LS == RS:
            return i
        LS += arr[i]

    return -1

arr = [-7, 1, 10, 12, -4, 3, 0]
n=len(arr)
print(arrayEquilibriumIndex(arr,n))
