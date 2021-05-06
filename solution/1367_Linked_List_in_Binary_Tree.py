# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 1
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(target: ListNode, node: TreeNode) :
            if not target : return True
            if not node : return False
            return (node.val == target.val) and (dfs(target.next, node.left) or dfs(target.next, node.right))
        
        return root and (dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right))

#     # Solution 2 (slow)
#     def is_sublist(self, l1: List, l2: List) -> bool :
#         if len(l1) < len(l2) : return False
#         elif l1 == l2 : return True
        
#         for i in range(len(l1)-len(l2)+1) :
#             if l1[i:i+len(l2)] == l2 :
#                 return True
#         return False
        
#     def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
#         solution = []
#         while head :
#             solution.append(head.val)
#             head = head.next
        
#         def dfs(node: TreeNode, path: List[int]) :
#             if not node :
#                 return self.is_sublist(path, solution)
#             return dfs(node.left, path+[node.val]) or dfs(node.right, path+[node.val])
        
#         return dfs(root, [])
        
