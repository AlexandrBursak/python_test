# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sub_sum = {}

        def sum_all_cousins(root, level):
            if level not in sub_sum:
                sub_sum[level] = 0
            if level > 1:
                sub_sum[level] += root.val

            if root.left:
                sum_all_cousins(root.left, level + 1)
            if root.right:
                sum_all_cousins(root.right, level + 1)

        sum_all_cousins(root, level=0)

        def redefine_the_sums_of_cousins(root, level):
            if level <= 1:
                root.val = 0

            cousins = 0
            if level + 1 in sub_sum:
                cousins = sub_sum[level + 1]

            if root.left:
                cousins -= root.left.val
            if root.right:
                cousins -= root.right.val

            if root.left:
                root.left.val = cousins
            if root.right:
                root.right.val = cousins

            if root.left:
                redefine_the_sums_of_cousins(root.left, level + 1)
            if root.right:
                redefine_the_sums_of_cousins(root.right, level + 1)

        redefine_the_sums_of_cousins(root, level=0)

        return root