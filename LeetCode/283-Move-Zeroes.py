"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

"""

# Solution 1: Brute: Time: O(n) Space: O(n)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        non_zero_elements = []

        for i in range(len(nums)):
            if nums[i] != 0:
                non_zero_elements.append(nums[i])
        
        non_zero_elements_length = len(non_zero_elements)

        for i in range(non_zero_elements_length):
            nums[i] = non_zero_elements[i]

        for i in range(non_zero_elements_length, len(nums)):
            nums[i] = 0

# Solution 2: Optimal: Time: O(n) Space: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i +=1
        
