"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(depth: int, now: 'Node') :
            if not now.children :
                return depth
            return max(dfs(depth+1, c) for c in now.children)
        
        return dfs(1, root) if root else 0
