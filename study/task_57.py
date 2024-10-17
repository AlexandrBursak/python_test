from typing import List
import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        max_active = 0
        active = 0

        heap = []
        for left, right in intervals:
            heapq.heappush(heap, (left, 1))
            heapq.heappush(heap, (right+1, -1))

        while heap:
            _, action = heapq.heappop(heap)
            active += action
            max_active = max(max_active, active)

        return max_active



    # def minGroups(self, intervals: List[List[int]]) -> int:
    #     max_active = 0
    #     active = 0

    #     action_list = []

    #     for left, right in intervals:
    #         action_list.append([left, 1])
    #         action_list.append([right+1, -1])
        
    #     action_list.sort()

    #     for _, action in action_list:
    #         active += action
    #         max_active = max(max_active, active)
    
    #     return max_active


    # Worked script but with Timeout limit
    # def minGroups(self, intervals: List[List[int]]) -> int:
    #     result = 0
    #     heap = []

    #     if len(intervals) == 1:
    #         return 1

    #     for i in intervals:
    #         heapq.heappush(heap, i)

    #     list_intervals = []
    #     while heap:
    #         pos_left, pos_right = heapq.heappop(heap)

    #         print(pos_left, pos_right)

    #         for i in range(result):
    #             if list_intervals[i] <= pos_left:
    #                 list_intervals[i] = pos_right + 1
    #                 break
    #         else:
    #             list_intervals.append(pos_right + 1)
    #             result += 1

    #     return result



solution = Solution()

intervatls = [[5,10],[6,8],[1,5],[2,3],[1,10]]
expected = 3

print(solution.minGroups(intervatls), '==', expected, ':', intervatls)

intervatls = [[1,3],[5,6],[8,10],[11,13]]
expected = 1

print(solution.minGroups(intervatls), '==', expected, ':', intervatls)

expected = 1

print(solution.minGroups(intervatls), '==', expected, ':', intervatls[:100])