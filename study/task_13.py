from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        full_list = sorted(nums1 + nums2)
        half_list_len = len(full_list)//2

        if len(full_list) % 2:
            median = full_list[half_list_len]
        else:
            median = (full_list[half_list_len-1] + full_list[half_list_len])/2

        return median

solution = Solution()
print(solution.findMedianSortedArrays([10,30,60], [20,40]))
print(solution.findMedianSortedArrays([10,30,60,50], [20,40]))