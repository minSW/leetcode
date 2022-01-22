# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, prev: int) -> int :
            if not node : return 0
            
            prev = max(node.val, prev)
            return (node.val == prev) + dfs(node.left, prev) + dfs(node.right, prev)
        
        return dfs(root, -10**4)
