import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)

            remains = stone_1 - stone_2
            if remains:
                if remains > 0:
                    remains = -remains
            heapq.heappush(stones, remains)

        return -stones[0]