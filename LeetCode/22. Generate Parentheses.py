"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

# Solution: Time: O(2^n * n) Space: O(2n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        def backtrack(open_count, close_count):
            if open_count == close_count == n:
                result.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()

            if open_count > close_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop()
        backtrack(0,0)
        return result
