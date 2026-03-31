class DynamicArray:
    
    def __init__(self, capacity: int):
        self._arr_ = [None] * capacity
        self._len_ = 0

    def get(self, i: int) -> int:
        return self._arr_[i]

    def set(self, i: int, n: int) -> None:
        self._arr_[i] = n

    def pushback(self, n: int) -> None:
        if self._len_ == len(self._arr_):
            self.resize()
        self._arr_[self._len_] = n
        self._len_ += 1

    def popback(self) -> int:
        to_return = self._arr_[self._len_ - 1]
        self._len_ -= 1
        return to_return

    def resize(self) -> None:
        new_arr = [None] * (2 * len(self._arr_))
        for i in range (self._len_):
            new_arr[i] = self._arr_[i]
        self._arr_ = new_arr

    def getSize(self) -> int:
        return self._len_
    
    def getCapacity(self) -> int:
        return len(self._arr_)