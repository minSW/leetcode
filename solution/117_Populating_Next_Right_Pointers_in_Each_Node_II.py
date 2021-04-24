"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root :
            return root
        
        queue = [(root, 1)]
        while queue :
            now, level = queue.pop(0)
            if now.left : queue.append((now.left, level+1))
            if now.right : queue.append((now.right, level+1))
            
            if queue and level == queue[0][1] :
                now.next = queue[0][0]
            else :
                now.next = None
        
        return root
        
