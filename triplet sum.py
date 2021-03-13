# def find3Numbers(A, arr_size, sum):
#     count = 0
#
#     for i in range(0, arr_size - 2):
#
#         for j in range(i + 1, arr_size - 1):
#
#             for k in range(j + 1, arr_size):
#                 if A[i] + A[j] + A[k] == sum:
#                     count = count + 1
#     print(count,end=" ")
#
#     return -1
# def tripletSum(arr, n, num) :
#     count = 0
#
#     for i in range(0, n-2):
#
#         for j in range(i + 1, n - 1):
#
#             for k in range(j + 1, n):
#                 if arr[i] + arr[j] + arr[k] == num:
#                     count = count + 1
#     return count
#
#
#
# A = [2,1,4,3,5,4,6,5,3]
# sum = 12
# arr_size = len(A)
# print(tripletSum(A, arr_size, sum))


def triplesum(arr,n,num):
    arr.sort()
    count = 0
    for i in range(n-1):
        l=i+1
        r=n-1
        while l<=r:
            if arr[i] + arr[l] + arr[r] == num :
                count = count + 1

                l = l + 1
                r = r - 1
            elif arr[i] + arr[l] + arr[r] < num :
                l = l + 1
            else:
                r = r-1

    print(count)




arr=[2,1,4,3,5,4,6,5,3]
n=len(arr)
num = int(input("enter the no."))
triplesum(arr,n,num)




