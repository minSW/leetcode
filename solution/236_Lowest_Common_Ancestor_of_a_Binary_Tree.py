# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root in (p, q): 
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q) 
        
        return root if left and right else left or right

#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         p_parent, q_parent = [], []
        
#         def dfs(node: 'TreeNode', path: []) :
#             if not node or (p_parent and q_parent) :
#                 return
            
#             if node == p : 
#                 p_parent.extend(path + [node])
#             elif node == q :
#                 q_parent.extend(path + [node])
            
#             dfs(node.left, path + [node])
#             dfs(node.right, path + [node])
        
#         dfs(root, [])
        
#         return [ a for a, b in zip(p_parent, q_parent) if a == b ][-1]

