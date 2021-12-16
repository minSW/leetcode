# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, grandEven: bool) :
            if not node :
                return 0
            else :
                res = dfs(node.left, node.val % 2 == 0) + dfs(node.right, node.val % 2 == 0)
                if grandEven :
                    res += node.left.val if node.left else 0
                    res += node.right.val if node.right else 0
                return res
        
        return dfs(root, False)
