"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Input: nums = [1,1,2,2,3,4]
Output: 4, nums = [1,2,3,4,_,_]
"""

# Solution: Optimal Time: O(n) Space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i +=1
                nums[i] = nums[j]

        return i + 1
