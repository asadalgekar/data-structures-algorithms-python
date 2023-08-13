"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

# Solution 1: Brute: Recrusive: Time: O(N), Space: O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

# Solution 2: Brute: Iterative: Time: O(N), Space: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
