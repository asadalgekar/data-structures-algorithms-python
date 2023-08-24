"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
"""

# Solution 1: Brute Time: O(nlogn) Space: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        current_count = 1
        longest = 0
        last_smaller = float("-inf")

        #sort the array
        nums.sort()
        for i in range(len(nums)):

            if nums[i] - 1 == last_smaller:
                current_count += 1
                last_smaller = nums[i]

            elif nums[i] != last_smaller:
                current_count = 1
                last_smaller = nums[i]

            if current_count > longest:
                longest = current_count

        return longest
      
# Solution 2: Optimal Time: O(n) Space: O(n)
  class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        current_count = 1
        longest = 0
        #create set of nums
        num_set = set(nums)  
        for i in range(len(nums)):
            if nums[i] - 1 not in num_set :
                current_element = nums[i]
                current_count = 1
            
                # if sequence, check next
                while current_element + 1 in num_set :
                    current_element +=1
                    current_count += 1
                
            if current_count > longest:
                longest = current_count

        return longest
