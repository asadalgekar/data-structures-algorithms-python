input = [2,3,4,1,6]

def insetionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1 
        while j >= 0 and arr[j + 1] < arr[j]:
            arr[j + 1] ,arr[j] = arr[j], arr[j + 1]
            j = j -1
    return arr

# Unsorted Array: 2,3,4,1,6
result = insetionSort(input) # Sorted Array: 1,2,3,4,6
