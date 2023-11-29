""" 
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
"""

# Solution 1: Brute: Time: O(n) Space: O(n) 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        temp = [0] * len(nums)

        for i in range(len(nums)):
            temp[(i + k) % len(nums)] = nums[i]
        
        nums[:] = temp

        return nums

# Solution 2: Optimal: Time: O(n) Space: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k=k%len(nums)
        nums[:] = nums[n - k:] + nums[:n - k]
        return nums
        
