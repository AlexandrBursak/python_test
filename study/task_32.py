from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n_dict = {}
        i = 1
        for num in sorted(set(arr)):
            n_dict[num] = i
            i += 1

        return [n_dict[el] for el in arr]


solution = Solution()

nums = [37,12,28,9,100,56,80,5,12]
expected = [5,3,4,2,8,6,7,1,3]

print(solution.arrayRankTransform(nums), '==', expected, ':', nums)