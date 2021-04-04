# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dfs (iterative)
    def isUnivalTree(self, root: TreeNode) -> bool:
        value, stack = root.val, [root]
        
        while stack :
            now = stack.pop(-1)
            if now.val != value :
                return False
            if now.left : stack.append(now.left)
            if now.right : stack.append(now.right)
        
        return True
    
    # dfs (recursive)
    # def isUnivalTree(self, root: TreeNode) -> bool:
    #     value = root.val
    #     def dfs(node: TreeNode) :
    #         if not node :
    #             return True
    #         return node.val == value and dfs(node.left) and dfs(node.right)
    #     return dfs(root)
 
