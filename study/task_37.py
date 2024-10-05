from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            for idx, item in enumerate(nums[:-1]):
                if idx == 0 or nums[idx] != nums[idx-1]:
                    chash = target - item
                    if chash in nums[idx+1:]:
                        res.append([item, chash])
            return res

        def kSum(nums: List[int], k: int, target: int) -> List[List[int]]:
            res = []

            if not nums:
                return res

            avarege_value = target/k
            if nums[0] > avarege_value or nums[-1] < avarege_value:
                return res

            if k == 2:
                return twoSum(nums, target)

            for idx in range(len(nums)):
                if idx == 0 or nums[idx] != nums[idx-1]:        
                    for subset in kSum(nums[idx+1:], k-1, target-nums[idx]):
                        print([nums[idx]], subset)
                        res.append([nums[idx]] + subset)
            
            return res

        return kSum(nums, 4, target)


solution = Solution()

nums = [1,0,-1,0,-2,2] 
target = 0
expected = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

print(solution.fourSum(nums, target), '==', expected, ':', nums)

nums = [2,2,2,2,2] 
target = 8
expected = [[2,2,2,2]]

print(solution.fourSum(nums, target), '==', expected, ':', nums)
