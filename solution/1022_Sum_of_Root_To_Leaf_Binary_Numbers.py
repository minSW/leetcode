# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, value: int) :
            if not node :
                return 0
            
            next_value = value * 2 + node.val
            if not node.left and not node.right :
                return next_value
            else :
                return dfs(node.left, next_value) + dfs(node.right, next_value)
        return dfs(root, 0)
