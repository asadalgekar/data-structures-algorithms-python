"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
"""

# Solution 1: Brute: Time: O(n), Space: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        for i in range(len(nums)):
            if i == 0:
                if nums[i] != nums[i + 1]:
                    return nums[0]
            if i == n - 1:
                if nums[n - 1] != nums[n - 2]:
                    return nums[n - 1]

            else:
                if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                    return nums[i]
        return -1

# Solution 2: Optimal: Time: O(log n), Space: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1: return nums[0]
        if nums[0] != nums[1] : return nums[0]
        if nums[n - 1] != nums[n - 2]: return nums[n - 1]

        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]: return nums[mid]
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1])or(mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                low = mid + 1
            else:
                high = mid - 1
  
         
