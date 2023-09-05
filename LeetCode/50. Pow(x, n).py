"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

# Solution: Optimal: Recursion: Time:O(log n) Space:O(log n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(m,n):
            if n == 0:
                return 1
            if n % 2 == 0:
                 return helper(m * m, n// 2)
            else:
                return m * helper(m * m, (n-1)// 2)
        
        power = helper(x, abs(n))

        if n > 0: return power
        else: return 1 / power

