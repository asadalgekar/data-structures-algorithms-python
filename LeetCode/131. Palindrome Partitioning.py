"""
Given a string s, partition s such that every substringof the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
"""

# Solution: Recursion, Bakctracking: Time: O(2^n) Space: O(n)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
      
        def backtrack(string, index):
            if index == len(s):
                result.append(substring[:])
                return
            
            for i in range(index, len(s)):
                if checkPallindrome(s, index, i):
                    substring.append(s[index : i + 1])
                    backtrack(string, i + 1)
                    substring.pop()

        def checkPallindrome(string, start, end):
            while start <= end:
                if string[start] != string[end]:
                    return False
                start +=1
                end -=1
            return True

        result = []
        substring=[]
        backtrack(s, 0)
        return result
