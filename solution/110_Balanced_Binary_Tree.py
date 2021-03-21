# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) != -1
    
    def height(self, target: TreeNode) -> int :
        if not target :
            return 0
        l, r = self.height(target.left), self.height(target.right)
        if l < 0 or r < 0 or abs(l - r) > 1 :
            return -1
        else :
            return max(l, r) + 1
