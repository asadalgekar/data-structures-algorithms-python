"""
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
"""

# Solution: Time: O(log n) Space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1

            else:
                ans = min(ans, nums[mid])
                high = mid - 1

        return ans
