# def pair_sum(arr,n,k):
#     count = 0
#     if n==1:
#         return
#     for i in range(n-1):
#         for j in range(i+1,n):
#             if arr[i] + arr[j] == k:
#                 count = count+1
#     return count
# arr = [1,3,6,2,5,4,3,2,4]
# n=len(arr)
# k = int(input("enter the no."))
# print(pair_sum(arr,n,k))

def pairsum(arr,n,k):
    arr.sort()
    leftindex = 0
    rightindex = n-1
    count = 0
    while leftindex<rightindex:
        if arr[leftindex] + arr[rightindex] == k:
            count = count+1
            leftindex = leftindex + 1
            rightindex = rightindex - 1
        elif arr[leftindex] + arr[rightindex] < k:
            leftindex=leftindex+1
        else:
            rightindex=rightindex-1
    return count
arr = [1,3,6,2,5,4,3,2,4]
n=len(arr)
k = int(input("enter the no."))
print(pairsum(arr,n,k))


