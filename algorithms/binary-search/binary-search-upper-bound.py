# Time: O(log n)
# Space: O(1)

def upperBound(input_array, target_value):
    low = 0  # Initialize low pointer
    high = len(input_array) - 1  # Initialize high pointer
    answer = len(input_array)  # Initialize answer as the maximum possible index
    
    while low <= high:                              # Binary search loop
        mid = (low + high) // 2                     # Calculate middle index
        
        if input_array[mid] > target_value:        # If mid element is greater than or equal to target
            answer = mid                            # Update answer to mid index
            high = mid - 1                          # Look for a smaller index on the left
        else:
            low = mid + 1                           # Look on the right
            
    return answer                                   # Return the lower bound index

input_array = [-1, 0, 3, 5, 9, 12]
target_value = 9
result = upperBound(input_array, target_value) # Output: 4
