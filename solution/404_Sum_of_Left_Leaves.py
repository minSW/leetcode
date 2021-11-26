# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        elif self.is_leaf(root.left) :
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else :
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
    
    def is_leaf(self, node: TreeNode) -> bool :
        return node and not node.left and not node.right
