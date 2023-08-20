"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""


#Solution 1: Brute: Time: O(n) Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        zero,one,two=0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            if nums[i] == 1:
                one += 1
            if nums[i] == 2:
                two += 1
        
        for i in range(0, zero):
            nums[i] = 0
        for i in range(zero, zero + one):
            nums[i] = 1
        for i in range(zero + one, len(nums)):
            nums[i] = 2

#Solution 2: Optimal: O(n) Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=mid=0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low +=1
                mid += 1

            elif nums[mid] == 1:
                mid += 1
            
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
