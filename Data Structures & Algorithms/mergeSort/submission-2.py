# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def mergeSortHelper(self, pairs: List[Pair], l: int, r: int):
        if r <= l:
            return
        
        m = (l + r) // 2

        self.mergeSortHelper(pairs, l, m)
        self.mergeSortHelper(pairs, m+1, r)

        self.merge(pairs, l, m, r)
    
    def merge(self, pairs: List[Pair], l: int, m: int, r: int):
        L = pairs[l : m + 1]

        l_ptr, r_ptr, p_ptr, len_l, len_r = 0, m + 1, l, m - l + 1, r - m + 1

        while l_ptr < len_l and r_ptr <= r:
            if L[l_ptr].key <= pairs[r_ptr].key:
                pairs[p_ptr] = L[l_ptr]
                l_ptr, p_ptr = l_ptr + 1, p_ptr + 1
            else:
                pairs[p_ptr] = pairs[r_ptr]
                r_ptr, p_ptr = r_ptr + 1, p_ptr + 1
        
        while l_ptr < len_l:
            pairs[p_ptr] = L[l_ptr]
            l_ptr, p_ptr = l_ptr + 1, p_ptr + 1
        
        while r_ptr <= r:
            pairs[p_ptr] = pairs[r_ptr]
            r_ptr, p_ptr = r_ptr + 1, p_ptr + 1
