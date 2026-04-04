from collections import defaultdict

class TimeMap:

    def __init__(self):
        self._map_ = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self._map_:
            self._map_[key] = [(timestamp, value)]
        else:
            self._map_[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self._map_:
            return ""
        
        timestamped_values = self._map_[key]
        l, r = 0, len(timestamped_values) - 1

        ans = ""

        while l <= r:
            mid = (l + r) // 2
            if timestamped_values[mid][0] == timestamp:
                return timestamped_values[mid][1]
            
            if timestamped_values[mid][0] < timestamp:
                ans = timestamped_values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return ans