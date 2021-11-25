# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        stack = [(root, 0)] 
        res, prev = 100000, -100000
        
        while stack :
            node, checked = stack.pop()
            if node and not checked :
                stack += [(node.right, 0), (node, 1), (node.left, 0)]
            elif checked :
                res, prev = min(res, node.val-prev), node.val
        
        return res
    
#     # inorder
#     def minDiffInBST(self, root: TreeNode) -> int:
#         sorted_list = []
        
#         def in_order(node: TreeNode) -> int :
#             if not node : return
            
#             in_order(node.left)
#             sorted_list.append(node.val)
#             in_order(node.right)
        
#         in_order(root)
#         return min(y-x for x, y in zip(sorted_list, sorted_list[1:]))
