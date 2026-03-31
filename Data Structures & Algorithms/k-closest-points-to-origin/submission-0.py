import heapq

class Solution:
    def distance_squared(self, point: List[List[int]]) -> int:
        return point[0] ** 2 + point[1] ** 2
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k: return points

        weighted_points = [(self.distance_squared(p), p) for p in points]
        heapq.heapify(weighted_points)
        
        return [heapq.heappop(weighted_points)[1] for _ in range(k)]