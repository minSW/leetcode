# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        stack = [(root, 1)]
        result = max_depth = 0
        
        # Use DFS
        while stack :
            now, depth = stack.pop(-1)
            
            if not now :
                continue
            elif not now.left and not now.right :
                if depth > max_depth :
                    max_depth = depth
                    result = now.val
                elif depth == max_depth :
                    result += now.val
                else :
                    continue
            stack.append((now.right, depth+1))
            stack.append((now.left, depth+1))
        return result
    
#     def deepestLeavesSum(self, root: TreeNode) -> int:
#         queue = [(root, 1)]
#         result = max_depth = 0
        
#         # Use Level-order Traversal
#         while queue :
#             now, depth = queue.pop(0)
#             if not now or depth < max_depth :
#                 continue
#             elif depth > max_depth :
#                 result = now.val
#                 max_depth = depth
#             elif depth == max_depth :
#                 result += now.val
            
#             queue.append((now.left, depth+1))
#             queue.append((now.right, depth+1))
#         return result
