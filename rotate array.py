# def rotatearray(array , n , d):
#     temp = []
#     i=0
#     while i < d:
#         temp.append(array[i])
#         i=i+1
#
#     i=0
#     while i<n:
#         array[i] = array[d]
#         d = d+1
#         i = i+1
#     array[:] = array[:i] + temp
#     return array
#
#
#
#
#
# arr = [1,2,3,4,5]
# print(rotatearray(arr,len(arr),2),end=" ")

# def left_rotate_by_one(arr, n):
#
#     temp = arr[0]
#
#
#     for i in range(n - 1):
#         arr[i] = arr[i + 1]
#         arr[n - 1] = temp
#
#
# def leftRotate(arr, d, n):
#     for i in range(0, d):
#         left_rotate_by_one(arr, n)
#
#
#
# arr =  [1, 2, 3, 4, 5, 6, 7]
# n = len(arr)
# no_of_rotations = int(input("enter no. of rotation"))
# print("Array Elements before rotation : ")
# for i in range(0, n):
#     print(arr[i], end=' ')
# leftRotate(arr, no_of_rotations, n)
# print("\nArray Elements after rotation : ")
# for i in range(0, n):
#     print(arr[i], end=' ')

def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr


# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))