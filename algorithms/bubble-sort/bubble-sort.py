# Time: Best:Ω(n)	Average:Θ(n^2) Best:O(n^2)	
# Space: O(1)

def bubble_sort(arr):
    size = len(arr)
    count = 0
    for i in range(size - 1):
        count+=1
        swaps = False
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
                swaps = True
        if swaps == False:
            break
    print(count)
