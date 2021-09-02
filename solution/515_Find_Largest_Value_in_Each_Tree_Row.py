# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root :
            queue = [root]

            while queue :
                res.append(max([ node.val for node in queue ]))
                queue = [ child for node in queue for child in [node.left, node.right] if child ]
        
        return res
    
    # recursive
#     def largestValues(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
        
#         def bfs(node: TreeNode, level: int) :
#             if len(res) <= level:
#                 res.append([])
            
#             res[level].append(node.val)
            
#             if node.left : bfs(node.left, level+1)
#             if node.right : bfs(node.right, level+1)
        
#         if root :
#             bfs(root, 0)
#         return [ max(values) for values in res ]
