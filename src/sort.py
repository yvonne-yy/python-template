import numpy
import time
from quicksort import quicksort

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def printArray(arr):
    for x in arr:
        print(x, end=' ')
    print()

def selectionSort(arr):
    for j in range(0, len(arr)):
        min_idx = j
        for i in range(j, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
        swap(arr,j, min_idx)
    #printArray(arr)

def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                swap(arr, j, j-1)
            else:
                break
    #printArray(arr)


def insertionSort2(arr):
    for i in range(1, len(arr)):    
        mem = arr[i]
        j = i
        while (j > 0 and mem < arr[j-1]):
            arr[j] = arr[j-1]
            j-=1
        arr[j] = mem
    #printArray(arr)

#in-place merge
def merge(arr, aux, low, mid, high):
    if arr[mid] <= arr[mid+1]:
        return
    i = low
    j = mid + 1
    #copy arr to aux
    for k in range(low, high+1):
        aux[k] = arr[k]
    #use aux to compare and put back into original array
    for k in range(low, high+1):
        if i > mid:
            arr[k] = aux[j]
            j+=1
        elif j > high:
            arr[k] = aux[i]
            i+=1
        elif aux[i] < aux[j]:
            arr[k] = aux[i]
            i+=1
        else:
            arr[k] = aux[j]
            j+=1

def sort(arr, aux, low, high):
    if(high <= low):
        return
    mid = low + int((high - low)/2)
    sort(arr, aux, low, mid)
    sort(arr, aux, mid+1, high)
    merge(arr, aux, low, mid, high)
    
def topDownMergeSort(arr):
    #copy the array to auxiliary array
    aux = []
    for x in arr:
        aux.append(x)
    sort(arr, aux, 0, len(arr)-1)
    #printArray(arr)



def timeSort(function_name, input_arr):
    start = time.time()
    if function_name == 'selectionSort':
        selectionSort(input_arr)
    if function_name == 'insertionSort':
        insertionSort(input_arr)
    if function_name == 'insertionSort2':
        insertionSort2(input_arr)
    if function_name == 'topDownMergeSort':
        topDownMergeSort(input_arr)
    if function_name == 'quicksort':
        quicksort(input_arr)
    end = time.time()
    #print(function_name +  "--- %s milliseconds ---" %(end-start)*1000)
    return end-start


def timeRandomInput(algs, N, T):
    num_algs = len(algs)
    t = [0.0] * num_algs
    for i in range(0, T):
        random_float_array = numpy.random.randint(1000, size = 50)
        for j in range(num_algs):
            t[j] += timeSort(algs[j], random_float_array)
    return dict(zip(algs,t))


def sortCompare():
    algs = ['insertionSort2', 'topDownMergeSort', 'quicksort']
    N = 1000
    T = 700
    #milliseconds
    print(timeRandomInput(algs, N, T))


    

testArray = [12,334,567,4,356,7655,4,5567,65]
#selectionSort(numpy.random.uniform(-100, 100, 10))
#insertionSort(numpy.random.uniform(-100, 100, 10))
#insertionSort2(numpy.random.uniform(-100, 100, 10))
#topDownMergeSort(numpy.random.uniform(-100, 100, 10))
#quicksort(numpy.random.uniform(-100, 100, 1000))


sortCompare()
