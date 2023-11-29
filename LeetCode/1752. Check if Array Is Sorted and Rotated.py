"""
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.

Input: nums = [3,4,5,1,2]
Output: true
"""

# Optimal Solution: Time: O(N) Space: O(1)
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for number in range(len(nums)):
            if nums[number] > nums[(number + 1) % len(nums)]:
                count +=1
        if count == 1:
            return True
        else:
            return False
