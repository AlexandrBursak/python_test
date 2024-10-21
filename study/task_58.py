from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        max_or = 0

        for num in nums:
            max_or |= num
            # print('max_or:', max_or)

        
        print('max_or:', max_or)

        def find_subset(i, curr_or):
            if i == len(nums):
                return 1 if max_or == curr_or else 0
            
            count_adds = find_subset(i+1, curr_or | nums[i])

            count_less = find_subset(i+1, curr_or)

            return count_adds + count_less

        return find_subset(0, 0)


solution = Solution()

nums = [3, 1]
expected = 2

print(solution.countMaxOrSubsets(nums), '==', expected, ':', nums)

nums = [3, 1, 5, 6]
expected = 2

print(solution.countMaxOrSubsets(nums), '==', expected, ':', nums)