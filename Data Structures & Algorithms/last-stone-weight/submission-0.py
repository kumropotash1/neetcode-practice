import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop_max(stones)
            stone_2 = heapq.heappop_max(stones)

            remains = stone_1 - stone_2
            if remains:
                if remains < 0:
                    remains = -remains
            heapq.heappush_max(stones, remains)

        return stones[0]