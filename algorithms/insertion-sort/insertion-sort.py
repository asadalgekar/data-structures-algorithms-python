# Time: Best: Ω(n) Average: Θ(n^2) Worst:O(n^2)	
# Space: O(1)

input = [2,3,4,1,6]

def insetionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1 
        while j >= 0 and arr[j + 1] < arr[j]:
            arr[j + 1] ,arr[j] = arr[j], arr[j + 1]
            j = j -1
    

# Unsorted Array: 2,3,4,1,6
insetionSort(input) # Sorted Array: 1,2,3,4,6
