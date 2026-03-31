# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs, s, e):
        if e <= s: return

        left = s
        pivot = pairs[e].key

        for i in range(s, e):
            if pairs[i].key < pivot:
                pairs[i], pairs[left] = pairs[left], pairs[i]
                left += 1
        
        pairs[e], pairs[left] = pairs[left], pairs[e]

        self.quickSortHelper(pairs, s, left - 1)
        self.quickSortHelper(pairs, left + 1, e)