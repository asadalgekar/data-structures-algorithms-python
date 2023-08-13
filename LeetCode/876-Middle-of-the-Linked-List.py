""" 
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

# Solution 1: Brute Force, Time: O(N + N/2), Space: O(1)
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        current = head
        while current:
            total +=1
            current = current.next

        current = head
        for i in range(total // 2):
            current = current.next
        return current

# Solution 2: Optimal, Time: O(N), Space: O(1)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
