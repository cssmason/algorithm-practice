from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        if head.val != head.next.val:
            prev = head
            head = self.deleteDuplicates(head.next)
            prev.next = head
            return prev
        else:
            value = head.val
            while head and head.val == value:
                head = head.next
            return self.deleteDuplicates(head)
