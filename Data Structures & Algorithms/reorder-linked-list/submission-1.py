# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 1
        node = head
        while node := node.next:
            length += 1
        
        if length <= 2:
            return
        
        to_be_reversed = head
        for i in range((length + 1) // 2 - 1):
            to_be_reversed = to_be_reversed.next
        
        temp = to_be_reversed
        to_be_reversed = to_be_reversed.next
        temp.next = None

        reversed_head = None
        while to_be_reversed:
            tmp = to_be_reversed
            to_be_reversed = to_be_reversed.next
            tmp.next = reversed_head
            reversed_head = tmp
        
        # temp.next = reversed_head

        node = head
        while reversed_head:
            tmp = reversed_head
            reversed_head = reversed_head.next
            node.next, tmp.next = tmp, node.next
            node = node.next.next