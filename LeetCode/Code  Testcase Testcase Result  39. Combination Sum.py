"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
"""

# Solution Time: O(2^n) Space: O(kx) where k = length of combination and x = no. of combinations
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(index, target):

            if target == 0:
                combinations.append(stack[:])
                return
            
            if index == len(candidates):
                return
            
            if candidates[index] <= target:
                stack.append(candidates[index])
                backtrack(index, target - candidates[index])
                stack.pop()  # Backtrack by removing the last element

            # Move to the next candidate
            backtrack(index + 1, target)
                 
        stack = []
        combinations = []
        backtrack(0, target )
        return combinations


            
