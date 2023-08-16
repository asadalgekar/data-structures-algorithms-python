# Time: 	Best:Ω(n log(n))	Average: Θ(n log(n))	Worst: O(n^2)
# Space: O(n^2)

def quickSort(arr, low, high):
    if low < high:
        partitioned_index = findPivot(arr, low, high)
        quickSort(arr, low, partitioned_index - 1)  # Sort the left subarray
        quickSort(arr, partitioned_index + 1, high)  # Sort the right subarray

def findPivot(arr, low, high):
    pivot = arr[low]  # Choose the first element as the pivot
    i = low + 1  # Initialize the index for elements to the right of the pivot
    j = high  # Initialize the index for elements to the left of the pivot
    
    while i <= j:  # Continue until the two indices meet or cross
        while i <= high and arr[i] <= pivot:
            i += 1  # Move to the right while elements are less than or equal to the pivot
            
        while j >= low + 1 and arr[j] > pivot:
            j -= 1  # Move to the left while elements are greater than the pivot
        
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]  # Swap the elements to maintain the partitioning
    
    arr[low], arr[j] = arr[j], arr[low]  # Place the pivot in its correct position
    return j  # Return the index of the pivot's final position

arr = [2, 2, 4, 1, 6]
quickSort(arr, 0, len(arr) - 1)  # Call quickSort to sort the entire array
# Output: Sorted array: [1, 2, 2, 4, 6]
