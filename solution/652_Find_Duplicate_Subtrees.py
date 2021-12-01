# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        node_dict = collections.defaultdict(list)
        
        def memPath(node: TreeNode) -> List[int] :
            path = [None]
            if node :
                path = [node.val] + memPath(node.left) + memPath(node.right)
                node_dict[tuple(path)].append(node)
            return path
        
        memPath(root)
        return [ nodes[0] for nodes in node_dict.values() if len(nodes) > 1 ]
