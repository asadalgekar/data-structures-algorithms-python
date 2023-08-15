
# Time: Best: Ω(n^2) Average: Θ(n^2) Worst:O(n^2)	
# Space: O(1)
input =[2, 3, 4, 1, 6]
def selectionSort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
   

# Unsorted Array: 2,3,4,1,6
selectionSort(input) #Sorted Array: 1,2,3,4,6
