from typing import Optional
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Copypast
    # def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
    #     queue = deque([(1, root)])

    #     print(queue)
    #     level_sum = defaultdict(int)
    #     while queue:
    #         level, current = queue.popleft()

    #         print(level, current)
    #         level_sum[level] += current.val
    #         if current.left:
    #             queue.append((level + 1, current.left))
    #         if current.right:
    #             queue.append((level + 1, current.right))
    #     if level < k:
    #         return -1
    #     return sorted(level_sum.values())[-k]
    
    # My script
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sum_of_level = defaultdict(int)

        def summarizeOfLevel(root, level):
            sum_of_level[level] += root.val

            if root.left:
                summarizeOfLevel(root.left, level + 1)
            if root.right:
                summarizeOfLevel(root.right, level + 1)

        summarizeOfLevel(root, 0)

        if k > len(sum_of_level):
            return -1
        return sorted(sum_of_level.values())[-k]
