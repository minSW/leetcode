# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, visited = [root], set()
        res = []
        while stack :
            now = stack.pop()
            if not now or now in visited :
                continue
            if (not now.left or now.left in visited) and (not now.right or now.right in visited) :
                res.append(now.val)
                visited.add(now)
            else :
                stack.extend([now, now.right, now.left])
        return res
    
    # # Recursive
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root :
    #         return []
    #     return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
