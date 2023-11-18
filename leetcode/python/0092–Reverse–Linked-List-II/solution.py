# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        leftPrev, curr = dummy, head
        for _ in range(left - 1):
            leftPrev, curr = curr, curr.next

        prev = None
        for _ in range(right - left + 1):
            tmpNext = curr.next
            curr.next = prev
            prev, curr = curr, tmpNext

        leftPrev.next.next = curr
        leftPrev.next = prev
        return dummy.next
