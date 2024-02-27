from del1Labb6 import *

def main():
    # index = indexlista()
    # test_index = index[:5]

    # print(heapsort(test_index))
    pass

def heapify(arr, n, i): # denna funktion gör om en lista till en heap
    largest = i # largest = root
    left = 2 * i + 1 # left = 2*i + 1
    right = 2 * i + 2 # right = 2*i + 2

    if left < n and arr[i] < arr[left]: # om left är mindre än n och arr[i] är mindre än arr[left]
        largest = left

    if right < n and arr[largest] < arr[right]: # om right är mindre än n och arr[largest] är mindre än arr[right]
        largest = right

    if largest != i: # om largest inte är i
        arr[i], arr[largest] = arr[largest], arr[i] # swap arr[i] and arr[largest]
        heapify(arr, n, largest) # heapify the root element again to make sure it's the largest element in the heap (max-heap)

# källa: https://www.geeksforgeeks.org/heap-sort/
def heapsort(arr): # denna funktion sorterar en lista med hjälp av en heap
    n = len(arr)

    # bygg en max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extrahera element ett efter ett
    for i in range(n - 1, 0, -1):  # n-1, n-2, n-3, ... 1
        arr[i], arr[0] = arr[0], arr[i]  # swap arr[i] and arr[0] (root) element in the heap
        heapify(arr, i, 0) # heapify root element

    return arr

main()