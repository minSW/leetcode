# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # preorder : root -> left -> right
    # recursive
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root : return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
    # # iterative
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     res, stack = [], [root]
    #     while stack :
    #         now = stack.pop()
    #         if now : 
    #             res.append(now.val)
    #             stack.append(now.right)
    #             stack.append(now.left)
    #     return res
