class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = None
    
    def get(self, index: int) -> int:
        ptr = self.head
        i = 0
        while i <= index:
            ptr = ptr.next
            i += 1
            if not ptr: return -1
        return ptr.val

    def insertHead(self, val: int) -> None:
        self.head.next = ListNode(val, self.head.next)
        if not self.tail:
            self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        if not self.tail:
            self.insertHead(val)
            return
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        ptr = self.head
        while i < index:
            ptr = ptr.next
            if not ptr: return False
            i += 1
        if not ptr.next: return False

        if self.tail == ptr.next:
            self.tail = ptr
        ptr.next = ptr.next.next
        return True

    def getValues(self) -> List[int]:
        res = []
        ptr = self.head.next

        while ptr:
            res.append(ptr.val)
            ptr = ptr.next
        
        return res

