# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        now, result = root, root.val
        
        while now:
            if abs(now.val - target) < abs(result - target):
                result = now.val
            
            if target < now.val :
                now = now.left
            else :
                now = now.right
        
        return result
