# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        sorted_list = list()
        
        def inorder(node: TreeNode) :
            if node :
                inorder(node.left)
                sorted_list.append(node.val)
                inorder(node.right)
        
        inorder(root)
        return min(sorted_list[i+1] - sorted_list[i] for i in range(len(sorted_list)-1))
            

#     def getMinimumDifference(self, root: TreeNode) -> int:
#         def getRightmostValue(self, node: TreeNode) -> int:
#             while node.right :
#                 node = node.right
#             return node.val

#         def getLeftmostValue(self, node: TreeNode) -> int:
#             while node.left :
#                 node = node.left
#             return node.val

#         mini = -1
#         nodeStack = [root]
#         while nodeStack :
#             now = nodeStack.pop(0)
#             if now.left :
#                 tmp = abs(now.val - getRightmostValue(now.left))
#                 if mini < 0 : mini = tmp
#                 else : mini = min(mini, tmp)
#                 nodeStack.append(now.left)
#             if now.right :
#                 tmp = abs(now.val - getLeftmostValue(now.right))
#                 if mini < 0 : mini = tmp
#                 else : mini = min(mini, tmp)
#                 nodeStack.append(now.right)
#         return mini
