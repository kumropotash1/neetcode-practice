class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]
        counts = defaultdict(int)

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        for n, c in counts.items():
            freqs[c].append(n)
        
        res = []

        for i in range(len(nums), 0, -1):
            freq = freqs[i]
            if freq:
                for n in freq:
                    res.append(n)
                    if len(res) == k:
                        return res