# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        to_be_reversed = slow.next
        slow.next = None

        reversed_head = None
        while to_be_reversed:
            tmp = to_be_reversed
            to_be_reversed = to_be_reversed.next
            tmp.next = reversed_head
            reversed_head = tmp

        node = head
        while reversed_head:
            tmp = reversed_head
            reversed_head = reversed_head.next
            node.next, tmp.next = tmp, node.next
            node = node.next.next