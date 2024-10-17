from typing import List
# from math import inf
# import heapq
from collections import defaultdict


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        merged = []

        # Merge all lists with their list index
        for i in range(len(nums)):
            for num in nums[i]:
                merged.append((num, i))
        
        print(merged)
        merged.sort()

        freq = defaultdict(int)
        left, count = 0, 0
        range_start, range_end = 0, float("inf")

        print(merged)
        for right in range(len(merged)):
            print(right)
            freq[merged[right][1]] += 1
            if freq[merged[right][1]] == 1:
                count += 1
            print(count)
            print(freq)

            while count == len(nums):
                cur_range = merged[right][0] - merged[left][0]
                if cur_range < range_end - range_start:
                    range_start = merged[left][0]
                    range_end = merged[right][0]

                freq[merged[left][1]] -= 1
                if freq[merged[left][1]] == 0:
                    count -= 1
                left += 1

        return [range_start, range_end]



    # def smallestRange(self, nums: List[List[int]]) -> List[int]:
    #     min_value = float(inf)
    #     max_value = float(-inf)
    #     substr = [float('-inf'), float('inf')]
    #     heap = []

    #     for i in range(len(nums)):
    #         heapq.heappush(heap, (nums[i][0], i, 0))
    #         max_value = max(max_value, nums[i][0])
        
    #     while heap:
    #         min_value, list_idx, i = heapq.heappop(heap)
    #         # print('heappop:', min_value, list_idx, i)
    #         if max_value - min_value < substr[1] - substr[0]:
    #             substr = [min_value, max_value]
    #         # print('substr:', substr)
            
    #         # print(i + 1, len(nums[list_idx]))
    #         if i + 1 < len(nums[list_idx]):
    #             nxt = nums[list_idx][i + 1]
    #             heapq.heappush(heap, (nxt, list_idx, i+1))
    #             max_value = max(max_value, nxt)
    #         else:
    #             break
        
    #     return substr


solution = Solution()

nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
expected = [20, 24]

print(solution.smallestRange(nums), '==', expected, ':', nums)

nums = [[1,2,3],[1,2,3],[1,2,3]]
expected = [1,1]

print(solution.smallestRange(nums), '==', expected, ':', nums)