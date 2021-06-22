# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        # pre : root -> left -> right
        # post : left -> right -> root
        
        if not pre :
            return None
        
        root = TreeNode(pre.pop(0))
        post.pop()
        
        if len(pre) > 0 :
            left_end = post.index(pre[0])
            root.left = self.constructFromPrePost(pre[:left_end+1], post[:left_end+1])
            root.right = self.constructFromPrePost(pre[left_end+1:], post[left_end+1:])
        
        return root
