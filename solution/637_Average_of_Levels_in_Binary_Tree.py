# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res, levels = [], [[root]]
        i = 0
        
        while levels[i] :
            nodes = levels[i]
            levels.append([])
            values = 0
            for node in nodes :
                if node.left : levels[i+1].append(node.left)
                if node.right : levels[i+1].append(node.right)
                values += node.val
            res.append(values/len(nodes))
            i += 1
        return res
        
            
