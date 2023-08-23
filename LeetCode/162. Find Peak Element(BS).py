"""
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""
# Solution 1: Brute: Time: O(n) Space: O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:return 0
        if nums[0] > nums[1]:return 0
        if nums[n - 1] > nums[n - 2]:return n - 1
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:return i
            
# Solution 2: Optimal: Time: O(log n) Space: O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:return 0
        if nums[0] > nums[1]:return 0
        if nums[n - 1] > nums[n - 2]:return n - 1
        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:return mid
            if nums[mid] > nums[mid - 1]:low = mid + 1
            else:high = mid - 1
                
