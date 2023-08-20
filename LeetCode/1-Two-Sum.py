"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Exmaple:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

# Solution 1: Brute: Time: O(n^2), Space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Solution 2: Optimal: Time: O(n), Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return hash_map[target - nums[i]], i

            hash_map[nums[i]] = i
