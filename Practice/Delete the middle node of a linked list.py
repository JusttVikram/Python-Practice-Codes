# Leetcode 2095
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head
    




# Another way to solve the problem


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If there's only one node, return None
        if head.next is None:
            return None
        
        link = None
        slow = head
        fast = head
        
        # Finding the middle node using slow and fast pointers
        while fast and fast.next:
            link = slow
            slow = slow.next
            fast = fast.next.next
        
        # Deleting the middle node by updating the link
        link.next = slow.next
        
        return head