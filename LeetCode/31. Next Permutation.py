"""
Given an array of integers nums, find the next permutation of nums.
Example:
Input: nums =[1,2,3,4]
Output: [1,2,4,3]
"""
# Solution 1: Brute: Recursive: Time: O(n! * n) Space: O(n)

# Solution 2: Optimal Time: O(3n) ~ O(n) Space: O(1)
class Solution:

    def reverse(self, arr, start, end):
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        break_point = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                break_point = i
                break
        if break_point == -1:
            return self.reverse(nums, 0, n - 1)
          
        for i in range(n-1, break_point, -1):
            if nums[i] > nums[break_point]:
                nums[break_point], nums[i] = nums[i], nums[break_point]
                break
        
        self.reverse(nums, break_point + 1, n - 1)
