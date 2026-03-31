class Node:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1, self.head)
        self.head.next = self.tail

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        n = Node(value, self.tail.prev, self.tail)
        self.tail.prev.next = n
        self.tail.prev = n

    def appendleft(self, value: int) -> None:
        n = Node(value, self.head, self.head.next)
        self.head.next.prev = n
        self.head.next = n

    def pop(self) -> int:
        if self.isEmpty(): return -1

        n = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

        return n.value

    def popleft(self) -> int:
        if self.isEmpty(): return -1

        n = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

        return n.value