# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth_dict = dict()
        
        def findLeaf(node: TreeNode, depth: int) -> TreeNode :
            if not node : return
            else : depth_dict[node.val] = depth
            
            left = findLeaf(node.left, depth+1)
            right = findLeaf(node.right, depth+1)
            
            if not left and not right :
                return node
            elif left and right :
                lv, rv = depth_dict[left.val], depth_dict[right.val]
                depth_dict[node.val] = max(lv, rv)
                if lv == rv : return node
                return left if lv > rv else right
            else :
                depth_dict[node.val] = depth_dict[left.val] if left else depth_dict[right.val]
                return left if left else right
            
        return findLeaf(root, 0)
        
        
#     def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
#         queue = [(root,0)]
#         res = collections.defaultdict(dict)
#         max_depth = 0
        
#         while queue :
#             node, depth = queue.pop(0)
#             if node.left :
#                 queue.append((node.left, depth+1))
#                 res[depth+1][node.left.val] = node
#             if node.right :
#                 queue.append((node.right, depth+1))
#                 res[depth+1][node.right.val] = node
#         if res :
#             max_depth = max(res.keys())
#             v = list(res[max_depth].values())
#             while max_depth > 0 :
#                 if len(v) == 1 :
#                     now = v.pop()
#                     return now.left or now.right
#                 elif len(set(v)) == 1:
#                     return v.pop()
#                 max_depth -= 1
#                 if max_depth :
#                     v = [res[max_depth][i.val] for i in v]
#         return root
