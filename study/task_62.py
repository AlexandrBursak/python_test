# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # My main logic, fast enough but not memory friendly
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        def levelValidation(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False

            result = True

            if root1.left:
                if not root2.left and not root2.right:
                    result = False
                elif root1.left and root2.left and root1.left.val == root2.left.val:
                    result = levelValidation(root1.left, root2.left)
                elif root1.left and root2.right and root1.left.val == root2.right.val:
                    result = levelValidation(root1.left, root2.right)
                else:
                    result = False
            
            if not result:
                return False
            
            if root1.right:
                if not root2.left and not root2.right:
                    result = False
                elif root1.right and root2.left and root1.right.val == root2.left.val:
                    result = levelValidation(root1.right, root2.left)
                elif root1.right and root2.right and root1.right.val == root2.right.val:
                    result = levelValidation(root1.right, root2.right)
                else:
                    result = False

            if (+(not root1.left) +(not root1.right) +(not root2.left) +(not root2.right)) %2 != 0:
                return False
            if not root1.left and not root1.right:
                if root2.left or root2.right:
                    return False
            
            return result

        return levelValidation(root1, root2)
