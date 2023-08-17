# Time: Best, Average, Worst:	Ω(n log(n))
# Space: O(n)

# Define the merge_sort function
def merge_sort(arr, low, high):
    if low < high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # Recursively sort the left and right halves
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        
        # Merge the sorted halves
        merge(arr, low, mid, high)

# Define the merge function to merge two sorted subarrays
def merge(arr, low, mid, high):
    temp = []  # Temporary list to store merged elements
    left = low  # Starting index of the left subarray
    right = mid + 1  # Starting index of the right subarray
    
    # Merge the two subarrays while comparing elements
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            # If the element in the left subarray is smaller or equal, add it to the temp list
            temp.append(arr[left])
            left += 1  # Move the index to the next element in the left subarray
        else:
            # If the element in the right subarray is smaller, add it to the temp list
            temp.append(arr[right])
            right += 1  # Move the index to the next element in the right subarray
    
    # Copy remaining elements from the left subarray (if any)
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    # Copy remaining elements from the right subarray (if any)
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    # Copy the sorted elements from temp back to the original array
    for i in range(len(temp)):
        arr[low + i] = temp[i]


arr = [2, 3, 4, 1, 6]
merge_sort(arr, 0, len(arr) - 1)  # Output: Sorted array: [1, 2, 3, 4, 6]
