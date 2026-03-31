# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeSortHelper(pairs, 0, len(pairs) - 1)

        return pairs
    
    def mergeSortHelper(self, pairs, l, r):
        if r <= l: return

        m = (l + r) // 2

        self.mergeSortHelper(pairs, l, m)
        self.mergeSortHelper(pairs, m + 1, r)

        self.merge(pairs, l, m, r)
    
    def merge(self, pairs, l, m, r):
        L = pairs[l: m + 1]

        len_l = m - l + 1
        # len_r = r - m

        i, j, k = 0, m + 1, l

        while i < len_l and j <= r:
            if L[i].key <= pairs[j].key:
                pairs[k] = L[i]
                i += 1
                k += 1
            else:
                pairs[k] = pairs[j]
                j += 1
                k += 1
        
        while i < len_l:
            pairs[k] = L[i]
            i += 1
            k += 1