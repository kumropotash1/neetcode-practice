# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._quicksort_(pairs, 0, len(pairs) - 1)
        return pairs
    def _quicksort_(self, pairs: List[Pair], s: int, e: int):
        if e <= s: return

        pivot = pairs[e].key
        left = s

        for i in range(s, e):
            if pairs[i].key < pivot:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1
        
        pairs[e], pairs[left] = pairs[left], pairs[e]

        self._quicksort_(pairs, s, left - 1)
        self._quicksort_(pairs, left + 1, e)
