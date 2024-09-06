# Leetcode 3217

from typing import List, Optional
from collections import ListNode

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        nums = set(nums)
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            if curr.val in nums:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next