# Solution 2: Convert into a min_heap of len k.
# Take negative of distance squared as weights.
# For every point, check if the current point is closer than the most distant point in the heapq (the top one)
# If yes, replace. If no, keep going.
# Essentially, we are converting a min_heap into a max_heap by taking the negatives of the weights.


import heapq

class Solution:
    def distance_squared(self, point: List[List[int]]) -> int:
        return point[0] ** 2 + point[1] ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k: return points

        min_heap = []

        for p in points:
            if len(min_heap) < k:
                heapq.heappush(min_heap, (-self.distance_squared(p), p))
            else:
                top_weight = min_heap[0][0]
                p_weight = -self.distance_squared(p)

                if p_weight > top_weight:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (p_weight, p))
        
        return [el[1] for el in min_heap]