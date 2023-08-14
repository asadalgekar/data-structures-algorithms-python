""" 
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
Do not modify the linked list.
"""
# Solution 1: Brute: Time: O(N), Space: O(N)
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        current = head

        while current:
            if current in visited:
                return current
            else:
                visited.add(current)
            current = current.next
        return None

# Solution 2: Optimal Time: O(N), Space: O(N)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
      
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
              
        if not fast or not fast.next:
            return None
                
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
