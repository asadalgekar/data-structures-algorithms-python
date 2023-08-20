"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
"""

# Solution 1: Optimal: Time: O(n) Space: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        prefix = count = 0

        for i in range(len(nums)):
            prefix += nums[i]

            if prefix - k in hashmap:
                count += hashmap[prefix - k]

            if prefix in hashmap:
                hashmap[prefix] += 1
            else:
                hashmap[prefix] = 1  

        return count
