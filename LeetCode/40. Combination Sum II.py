"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""
# Solution: Time: O(2^n) Space: O(kx) where k = no. of comibinations x = length of combinations
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(index, target):

            if target == 0:
                ans.append(ds[:])
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates and make sure dont compare with self

                if candidates[i] > target:
                    break

                ds.append(candidates[i])
                backtrack(i + 1, target - candidates[i])
                ds.pop()

        ans = []
        ds = []
        candidates.sort()
        backtrack(0, target)
        return ans
