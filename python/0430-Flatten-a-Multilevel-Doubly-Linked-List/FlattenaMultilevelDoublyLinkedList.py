"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(head: 'Optional[Node]') -> 'Optional[Node]':
            node = head
            while node:
                if node.child:
                    child = dfs(node.child)
                    if node.next:
                        node.next.prev = child.prev
                    child.prev.next = node.next
                    child.prev = node
                    node.next = child
                    node.child = None
                head.prev = node
                node = node.next
            return head

        if head is None:
            return None
        
        dfs(head).prev = None
        return head


        