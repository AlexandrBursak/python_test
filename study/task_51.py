from typing import List
from operator import itemgetter

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chairs = {}

        sorted_times = sorted(
            [(arrival, leaving, index) for index, (arrival, leaving) in enumerate(times)]
        )

        print(sorted_times)

        # for i in range(len(sorted_times)):
            


    # def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
    #     chairs = {}

    #     targetFriendTime = times[targetFriend]

    #     times_sorted = sorted(times, key=itemgetter(0))

    #     for friend in times_sorted:
    #         occupy = len(chairs)

    #         for chair in chairs:
    #             if chairs[chair] <= friend[0]:
    #                 chairs[chair] = friend[1]
    #                 occupy = chair
    #                 break
    #         else:
    #             chairs[occupy] = friend[1]

    #         if friend == targetFriendTime:
    #             return occupy


solution = Solution()

nums = [[1,4],[2,3],[4,6]]
targetFriend = 1
expected = 1

print(solution.smallestChair(nums, targetFriend), '==', expected, ':', targetFriend, nums)

nums = [[3,10],[1,5],[2,6]]
targetFriend = 0
expected = 2

print(solution.smallestChair(nums, targetFriend), '==', expected, ':', targetFriend, nums)

nums = [[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]]
targetFriend = 6
expected = 2

print(solution.smallestChair(nums, targetFriend), '==', expected, ':', targetFriend, nums)