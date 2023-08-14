"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Example 1:
Input: head = [1,2,2,1]
Output: true
# Example 2:
Input: head = [1,2]
Output: false
"""
# Solution 1: Brute: Time: O(N), Space: O(N)
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values == values[::-1]

# Solution 2: Optimal: Time: O(N), Space: O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        #middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse 2nd half
        previous = None
        while slow:
            next_node = slow.next
            slow.next = previous
            previous = slow
            slow = next_node

        # compare 1st hald, 2nd half
        first_half = head
        second_half = previous

        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True
