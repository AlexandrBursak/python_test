from typing import List
import time

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def parse_minute(time: str) -> int:
            h, m = map(int, time.split(":"))
            return m + h * 60

        points = sorted([parse_minute(time) for time in timePoints])
        points.append(points[0] + 24 * 60)

        min_minute = float("inf")
        for i in range(len(points) - 1):
            min_minute = min(min_minute, points[i + 1] - points[i])

        return min_minute
    

solution = Solution()

time = ["23:59","00:00"]
expected = 1

print(solution.findMinDifference(time), '==', expected, ':', time)

time = ["00:00","23:59","00:00"]
expected = 0

print(solution.findMinDifference(time), '==', expected, ':', time)

time = ["02:39","10:26","21:43"]
expected = 296

print(solution.findMinDifference(time), '==', expected, ':', time)
