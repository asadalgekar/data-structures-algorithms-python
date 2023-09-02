"""
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.

Example 1:
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
"""

# Solution: Optimal: Time: O(N * log(sum(arr[])-max(arr[])+1)), Space: O(1)
class Solution:
    def subArray(self, nums, checkSum):
        array = 1
        total_sum = 0
        for i in range(len(nums)):
            if total_sum + nums[i] <= checkSum:
                total_sum += nums[i]
            else:
                array += 1
                total_sum = nums[i]
        return array
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2
            totalSubArray = self.subArray(nums, mid)
            if totalSubArray > k:low = mid + 1
            else: high = mid - 1
        return low
