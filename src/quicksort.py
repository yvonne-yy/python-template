import random

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high
    while i < j:
        while arr[i] <= p:
            i += 1
            if i >= high:
                break
        while arr[j] >= p:
            j -= 1
            if j <= low + 1:
                break
        if arr[j] < arr[i]:
            swap(arr, i, j)
    if arr[low] > arr[j]:
        swap(arr, low, j)
    return j
      


def printArray(arr):
    for x in arr:
        print(x, end=' ')
    print()

def quicksort(arr):
    #printArray(arr)
    random.shuffle(arr)
    sort(arr, 0, len(arr)-1)
    #print('\nsorted\n')
    #printArray(arr)

def sort(arr, low, high):
    if high <= low:
        return
    p = partition(arr, low, high)
    if p == low:
        sort(arr, p+1, high)
    elif p == high:
        sort(arr, low, p-1)
    else:
        sort(arr, low, p-1)
        sort(arr, p+1, high)