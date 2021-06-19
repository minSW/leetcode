# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def getMaxLevel(node: TreeNode) -> int :
            if not node : return 0
            return 1 + getMaxLevel(node.left)
        def countOfPBTByLevel(level: int) -> int :
            return 2 ** (level + 1) - 1
        
        if not root :
            return 0
        ll, rl = getMaxLevel(root.left), getMaxLevel(root.right)
        if ll == rl : # left = perfect binary tree
            return 1 + countOfPBTByLevel(ll-1) + self.countNodes(root.right)
        else : # right = perfect binary tree
            return self.countNodes(root.left) + 1 + countOfPBTByLevel(rl-1)
    
#     # O(n) solution
#     def countNodes(self, root: TreeNode) -> int:
#         if not root :
#             return 0
        
#         now = root
#         level, level_stack = 0, [now]
        
#         while now.left :
#             level_stack = [ x for node in level_stack for x in (node.left, node.right) if x ]
#             level += 1
#             now = now.left
        
#         return 2 ** level - 1 + len(level_stack)
