from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                current = nums[i] + nums[j] + nums[k]
                if abs(current - target) < abs(closest - target):
                    closest = current


                if current < target:
                    j += 1
                elif current > target:
                    k -= 1
                else:
                    return current

        return closest

solution = Solution()

nums = [-1,2,1,-4]
target = 1
expected = 2

print(solution.threeSumClosest(nums, target), '==', expected, ':', nums)

nums = [0,0,0]
target = 1
expected = 0

print(solution.threeSumClosest(nums, target), '==', expected, ':', nums)

nums = [0,1,2]
target = 3
expected = 3

print(solution.threeSumClosest(nums, target), '==', expected, ':', nums)

nums = [1,1,1,0]
target = -100
expected = 3

print(solution.threeSumClosest(nums, target), '==', expected, ':', nums)

nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2
expected = -2

print(solution.threeSumClosest(nums, target), '==', expected, ':', nums)

nums = [-4,2,2,3,3,3]
target = 0
expected = 0

print(solution.threeSumClosest(nums, target), '==', expected, ':', nums)
