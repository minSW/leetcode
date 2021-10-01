# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [root]
        
        if root : 
            while stack :
                res.append(stack[0].val)
                stack = [ child for node in stack for child in (node.right, node.left) if child ]
        
        return res
