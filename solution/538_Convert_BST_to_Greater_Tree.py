# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # right -> root -> left
        def reverse_inorder(node: TreeNode, value: int) -> int:
            if not node : 
                return value
            right = reverse_inorder(node.right, value)
            node.val += right
            return reverse_inorder(node.left, node.val)
        
        reverse_inorder(root, 0)
        
        return root
