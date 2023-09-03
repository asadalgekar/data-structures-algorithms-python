"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2: Edge Case:
Input: nums = [3.-1,2,3,3,3,5]
"""

# Solution: Time: Bestm Avg: O(log n), Worst (All Duiplicats): O(n / 2)

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low+=1
                high-=1
                continue
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False
