class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleets = 1
        prev_time = (target - pair[0][0]) / pair[0][1]

        for i in range(1, n):
            time = (target - pair[i][0]) / pair[i][1]
            if time > prev_time:
                fleets += 1
                prev_time = time
        return fleets