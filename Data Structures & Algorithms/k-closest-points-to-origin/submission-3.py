# Solution 2: Convert into a max_heap of len k.
# Take distance squared as weights.
# For every point, check if the current point is closer than the most distant point in the heapq (the top one)
# If yes, replace. If no, keep going.
# At the end, we'll have a max_heap of len k with top = kth distant point


import heapq

class Solution:
    def distance_squared(self, point: List[List[int]]) -> int:
        return point[0] ** 2 + point[1] ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k: return points

        max_heap = []

        for p in points:
            if len(max_heap) < k:
                heapq.heappush_max(max_heap, (self.distance_squared(p), p))
            else:
                top_weight = max_heap[0][0]
                p_weight = self.distance_squared(p)

                if p_weight < top_weight:
                    heapq.heappop_max(max_heap)
                    heapq.heappush_max(max_heap, (p_weight, p))
        
        return [el[1] for el in max_heap]