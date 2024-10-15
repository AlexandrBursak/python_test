from typing import List
import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [num * -1 for num in nums]

        heapq.heapify(heap)

        count = 0
        while k > 0:
            k -= 1

            largest_num = heapq.heappop(heap) * -1
            count += largest_num

            heapq.heappush(heap, math.ceil(largest_num/3) * -1)

        return count







solution = Solution()

nums = [10,10,10,10,10]
k = 5
expected = 50

print(solution.maxKelements(nums, k), '==', expected, ':', k, nums)

nums = [1,10,3,3,3]
k = 3
expected = 17

print(solution.maxKelements(nums, k), '==', expected, ':', k, nums)