"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        old_to_copy_map = {}
        ptr = head
        while ptr:
            old_to_copy_map[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        ptr = head
        while ptr:
            if ptr.next:
                old_to_copy_map[ptr].next = old_to_copy_map[ptr.next]
            if ptr.random:
                old_to_copy_map[ptr].random = old_to_copy_map[ptr.random]
            ptr = ptr.next
        
        return old_to_copy_map[head]