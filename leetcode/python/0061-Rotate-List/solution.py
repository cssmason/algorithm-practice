from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        curr, length = head, 0
        while curr:
            length += 1
            prev, curr = curr, curr.next
        else:
            prev.next = head

        count = length - (k % length)

        for _ in range(count):
            prev, head = head, head.next
        prev.next = None
        return head
