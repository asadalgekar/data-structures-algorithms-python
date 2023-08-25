"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4
"""

# Solution: Optimal: Time: O(n * log n) Space: O(1)
class Solution:
    def findHours(self, piles, h):
        totalH = 0
        for i in range(len(piles)):
            totalH += math.ceil(piles[i] / h)
        return totalH

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_piles = max(piles)
        low = 1
        high = max_piles
        ans = max_piles

        while low <= high:
            mid = (low + high) // 2
            bananas_per_hour = self.findHours(piles,mid)
            if bananas_per_hour <= h:
                ans = mid  # Update ans with the current mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
