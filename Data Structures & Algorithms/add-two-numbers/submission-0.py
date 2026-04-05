# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = l1
        while True:
            new_val = l1.val + l2.val + carry
            l1.val, carry = new_val % 10, new_val // 10
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
            else:
                l1.next = l1.next or l2.next
                break

        while carry:
            if not l1.next:
                l1.next = ListNode(carry)
                carry = 0
            else:
                l1 = l1.next
                new_val = l1.val + carry
                l1.val, carry = new_val % 10, new_val // 10
        return head
