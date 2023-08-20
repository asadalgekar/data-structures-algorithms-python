"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1
"""

#Solution 1: Brute: Time:O(n) Space: O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_set = set()
        
        for i in range(len(nums)):
            if nums[i] not in num_set:
                num_set.add(nums[i])

            else:
                num_set.remove(nums[i])

        return next(iter(num_set))

#Solution 2: Optimal: Time:O(n) Space: O(1)
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
      res = 0

      for i in nums:
          res ^= i
      return res
