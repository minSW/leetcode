# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(pp: TreeNode, qp: TreeNode) -> bool :
            if not pp and not qp :
                return True
            elif xor(pp == None, qp == None) or  pp.val != qp.val :
                return False
            return dfs(pp.left, qp.left) and dfs(pp.right, qp.right)
        
        return dfs(p, q)
