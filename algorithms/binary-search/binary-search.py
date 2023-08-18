# Time: Best: O( log n)
# Space: O(1)

def binarySearch(arr, target):
    low = 0                            # Initialize the low pointer to the first index of the array.
    high = len(arr) - 1                # Initialize the high pointer to the last index of the array.
    
    while low <= high:                 # Perform binary search until the low pointer crosses the high pointer.
        mid = (low + high) // 2        # Calculate the middle index of the current range.
        
        if target > arr[mid]:          # If the target is greater than the middle element:
            low = mid + 1              # Move the low pointer to the right of the middle element.
        elif target < arr[mid]:        # If the target is smaller than the middle element:
            high = mid - 1             # Move the high pointer to the left of the middle element.
        else:                          # If the target is equal to the middle element:
            return mid 
    
    return -1                          # If the target is not found in the array, return -1.


input_array = [-1, 0, 3, 5, 9, 12]
target_value = 9
result = binarySearch(input_array, target_value) # Output: Target found at index: 4

