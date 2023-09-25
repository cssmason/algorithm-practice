# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = None
        slow = fast = head
        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow.next, reverse, slow = reverse, slow, slow.next
        if fast:
            slow = slow.next
        # check palindrome
        while reverse and reverse.val == slow.val:
            slow = slow.next
            reverse = reverse.next
        return not reverse
