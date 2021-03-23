# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root :
            return 0
        elif not root.left :
            return self.minDepth(root.right) + 1
        elif not root.right :
            return self.minDepth(root.left) + 1
        else :
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

#     def minDepth(self, root: TreeNode) -> int:
#         if not root :
#             return 0
        
#         stack = [(root, 1)]
#         while stack :
#             now = stack.pop(0)
#             if not now[0] :
#                 continue
#             elif not now[0].left and not node.right :
#                 return now[1]
#             else :
#                 stack.append((now[0].left, now[1]+1))
#                 stack.append((now[0].right, now[1]+1))
