"""
Given an integer array nums that may contain duplicates, return all possible 
subsets(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""

# Solution: Optimal: Time: O(2^n + n) Space: O(2^n * k)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subSet(index):
            ans.append(ds[:])
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i-1]:
                    continue
                ds.append(nums[i])
                subSet(i + 1)
                ds.pop()
                
        nums.sort()
        ans,ds=[],[]
        subSet(0)
        return ans
