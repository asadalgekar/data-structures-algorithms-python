"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
# Solution 1: Brute: Time: O(n) Space: O(1)
class Solution:
    def searchRange(self,nums, target):
        start = -1
        end = -1

        for i in range(len(nums)):
            if nums[i] == target:
                if start == -1:
                    start = i
                end = i

        return [start, end]

# Solution 2: Optimal: Time: O(log n) Space: O(1)
class Solution:

    def lowerBound(self, nums, target, n):
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def upperBound(self, nums, target, n):
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def searchRange(self, nums, target):
        n = len(nums)
        lower = self.lowerBound(nums, target, n)
        upper = self.upperBound(nums, target, n)

        if lower == n or nums[lower] != target:  # Corrected the condition here
            return [-1, -1]
        return [lower, upper - 1]
