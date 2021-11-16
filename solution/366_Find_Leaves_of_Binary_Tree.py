# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_depth = collections.defaultdict(list)
        
        def post_order(node: TreeNode) -> int :
            if not node :
                return 0
            
            depth = max(post_order(node.left), post_order(node.right))
            node_depth[depth].append(node.val)
            return depth + 1
        
        post_order(root)
        
        return [ node_depth[x] for x in sorted(node_depth.keys()) ]
