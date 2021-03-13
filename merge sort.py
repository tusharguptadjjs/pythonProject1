def mergeSort(arr,arr2):

        mergeSort(arr)
        mergeSort(arr2)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    arr2 = [2, 4, 2, 1, 4, 2, 1,7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr,arr2)
    print("Sorted array is: ", end="\n")
    printList(arr)