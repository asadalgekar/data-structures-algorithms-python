"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
"""

# Solution: Brute Time: O(n) Space: O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        missing = 0

        while 1:
            if num not in arr:
                missing += 1
                if missing == k:
                    return num

            num += 1

# Solution: Optimal Time: O(log n) Space: O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            total_missing_numbers = arr[mid] - (mid + 1)
            if total_missing_numbers < k:
                low = mid + 1

            else:
                high = mid - 1
        
        return k + high + 1
