"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
"""

# Solution 1: 2 Pass, Time: O(N), Space: O(1)
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        current = head
        while current:
            total +=1
            current = current.next
        # remove the first node from the lis
        if n == total:
            return head.next
        current = head
        for i in range(total - n - 1):
            current = current.next
        current.next = current.next.next
        return head

# Solution 1: 2 Pass, Time: O(N), Space: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=fast=head

        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
