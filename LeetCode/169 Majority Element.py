"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

# Solution 1: Brute: Time: O(n) Space: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmap={}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1

            else:
                hashmap[nums[i]] = 1

        for number, count in hashmap.items():
            if count > len(nums) / 2:
                return number

# Solution 2: Optimal: Time: O(n) Space: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0

        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count = 1
            
            elif nums[i] == candidate:
                count+=1
            else:
                count -=1

        majority = 0
        for i in range(len(nums)):
            if nums[i] == candidate:
                majority +=1
        if majority > len(nums)/2:
            return candidate
    
