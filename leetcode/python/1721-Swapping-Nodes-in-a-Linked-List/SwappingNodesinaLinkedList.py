# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = last = head
        for _ in range(1, k):
            first = first.next
        fast = first

        while fast.next:
            fast = fast.next
            last = last.next
        first.val, last.val = last.val, first.val
        return head
