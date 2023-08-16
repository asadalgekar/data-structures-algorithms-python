# Time: Best, Average, Worst:	Ω(n log(n))
# Space: O(n)

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2  # Parentheses added around the division
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid:  # Removed the extra space between '<' and '='
        temp.append(arr[left])
        left += 1
    while right <= high:  # Added missing 'arr'
        temp.append(arr[right])
        right += 1
    
    # Copy the sorted elements from temp back to the original array
    for i in range(len(temp)):
        arr[low + i] = temp[i]


arr = [2, 3, 4, 1, 6]
merge_sort(arr, 0, len(arr) - 1)  # Output: Sorted array: [1, 2, 3, 4, 6]
