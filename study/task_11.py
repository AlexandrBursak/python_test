from typing import List

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(0, len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             print("i, j, nums[i] + nums[j]", i, j, nums[i] + nums[j])
    #             if ((nums[i] + nums[j]) == target):
    #                 return i, j
        
    #     return []

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     res = {}
    #     for i in range(len(nums)):
    #         if nums[i] in res:
    #             return res[nums[i]], i
    #         chash = target-nums[i]
    #         res[chash] = i


    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     res = {}
    #     for idx, item in enumerate(nums):
    #         if item in res:
    #             return res[item], idx
    #         chash = target - item
    #         res[chash] = idx

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, item in enumerate(nums):
            find = target-item
            if find in nums[idx+1:]:
                return idx, nums[idx+1:].index(find)+idx+1


def main():
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))
    print(solution.twoSum([3,2,4], 6))
    print(solution.twoSum([3,3], 6))
    print(solution.twoSum([3,0,3], 6))

main()