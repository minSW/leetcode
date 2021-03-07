# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.toGstWithSum(root, 0)
        return root
    
    def toGstWithSum(self, node: TreeNode, val: int) -> int :
        if node.right :
            node.val += self.toGstWithSum(node.right, val)
        else :
            node.val += val
        
        if node.left :
            return self.toGstWithSum(node.left, node.val)
        else :
            return node.val

