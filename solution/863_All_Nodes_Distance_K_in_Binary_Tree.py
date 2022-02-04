# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        value_path = dict()
        
        def dfs(node: TreeNode, binary: str) :
            value_path[node.val] = binary
            if node.left : dfs(node.left, binary + "0")
            if node.right : dfs(node.right, binary + "1")
        
        def diff(target_path: str, path: str) -> int :
            t, p = len(target_path), len(path)
            for i in range(t) :
                if i == p : return t - i
                elif target_path[i] != path[i] : return (t - i) + (p - i)
            return p - t
        
        dfs(root, "")
        path = value_path[target.val]
        
        return [ key for key, value in value_path.items() if diff(path, value) == k ]
