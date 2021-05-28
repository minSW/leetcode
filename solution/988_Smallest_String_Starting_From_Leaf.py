# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(node: TreeNode, path: str) -> str :
            val = chr(node.val + ord('a'))
            if not node.left and not node.right : 
                return val + path
            
            res = []
            if node.left : res.append(dfs(node.left, val + path))
            if node.right : res.append(dfs(node.right, val + path))
            
            return min(res)
        
        return dfs(root, "")
       
# Slow Solution
#     def smallestFromLeaf(self, root: TreeNode) -> str:
#         def smaller(path1: list, path2: list) -> list :
#             if len(path1) == 0 : return path2
#             elif len(path2) == 0 : return path1
            
#             for x, y in zip(path1, path2) :
#                 if x < y : return path1
#                 elif x > y : return path2
#             return path1 if len(set(path1)) < len(set(path2)) else path2
            
#         def dfs(node: TreeNode, path: list) -> list :
#             if not node : return []
#             elif not node.left and not node.right : return [node.val] + path
#             return smaller(dfs(node.left, [node.val] + path), dfs(node.right, [node.val] + path))
        
#         return "".join([chr(x + ord('a')) for x in dfs(root, [])])
