class MinHeap:
    
    def __init__(self):
        self.__minheap__ = [None]

    def push(self, val: int) -> None:
        self.__minheap__.append(val)

        i = len(self.__minheap__) - 1
        while i > 1 and self.__minheap__[i] < self.__minheap__[i // 2]:
            self.__minheap__[i], self.__minheap__[i // 2] = self.__minheap__[i // 2], self.__minheap__[i]
            i //= 2

    def pop(self) -> int:
        if len(self.__minheap__) < 2:
            return -1

        if len(self.__minheap__) == 2:
            return self.__minheap__.pop(-1)

        else:
            res = self.__minheap__[1]
            self.__minheap__[1] = self.__minheap__.pop(-1)
            i = 1
            while i * 2 < len(self.__minheap__): # todo
                ptr = i * 2
                if len(self.__minheap__) > (ptr + 1) and self.__minheap__[ptr + 1] < self.__minheap__[ptr]:
                    ptr += 1
                if self.__minheap__[i] > self.__minheap__[ptr]:
                    self.__minheap__[i], self.__minheap__[ptr] = self.__minheap__[ptr], self.__minheap__[i]
                    i = ptr
                else: break
            return res

    def top(self) -> int:
        return self.__minheap__[1] if len(self.__minheap__) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.__minheap__ == [None]
        for n in nums:
            self.push(n)

        