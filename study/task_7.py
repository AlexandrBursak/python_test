# Реалізуйте функцію для перевірки збалансованості двійкового пошуку. Збалансоване дерево - це дерево, в якому висота піддерев різниться не більше ніж на одиницю.

# Приклад:
# Вхід:
#    1
#   / \
#  2   3
#     / \
#    4   5
# Вихід: True (збалансоване дерево)

# Вхід:
#    1
#   / 
#  2   
#   \
#    3
# Вихід: False (незбалансоване дерево)
# Це завдання перевіряє знання структур даних, таких як дерева, та вміння рекурсивно обминати їх.

class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root):

    def height(level):
        print('--- New loop ---')
        print(level)
        if level is None:
            print('return 0')
            return 0
        
        level_left = height(level.left)
        level_right = height(level.right)

        print("level_left, level_right:", level_left, level_right)

        if level_left == -1 or level_right == -1 or abs(level_left - level_right) > 1:
            return -1
        
        return 1 + max(level_left, level_right)

    return height(root) != -1


root_balanced = TreeNode(1)
root_balanced.left = TreeNode(2)
root_balanced.right = TreeNode(3)
root_balanced.left.left = TreeNode(4)
root_balanced.left.right = TreeNode(5)

print(is_balanced(root_balanced))

root_unbalanced = TreeNode(1)
root_unbalanced.right = TreeNode(2)
root_unbalanced.right.left = TreeNode(3)

print(is_balanced(root_unbalanced))
