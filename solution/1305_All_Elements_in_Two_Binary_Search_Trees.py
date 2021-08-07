# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inOrder(node: TreeNode, stack: List[int]) -> List[int]:
            if not node :
                return
            inOrder(node.left, stack)
            stack.append(node.val)
            inOrder(node.right, stack)
        
        res, stack1, stack2 = [], [], []
        inOrder(root1, stack1)
        inOrder(root2, stack2)
        
        while stack1 and stack2 :
            if stack1[0] <= stack2[0] :
                res.append(stack1.pop(0))
            else :
                res.append(stack2.pop(0))
        return res + stack1 + stack2

