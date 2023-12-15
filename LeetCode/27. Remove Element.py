"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
"""

# Solution 1 Brute: Time O(n) Space: O(n)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        for number in nums:
            if number != val:
                temp.append(number)

        for i in range(len(temp)):
            nums[i] = temp[i]
        
        return(len(temp))

# Solution 1 Optimal: Time O(n) Space: O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i
