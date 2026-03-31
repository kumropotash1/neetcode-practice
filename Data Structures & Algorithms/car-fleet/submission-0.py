class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position, speed))
        combined.sort(key = lambda el: -el[0])

        fleets = 1
        max_time = (target - combined[0][0]) / combined[0][1]

        for i in range(1, len(combined)):
            time = (target - combined[i][0]) / combined[i][1]
            if time > max_time:
                max_time = time
                fleets += 1
        return fleets