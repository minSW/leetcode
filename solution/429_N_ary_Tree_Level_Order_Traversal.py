"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root : 
            return list()
        
        result, queue = list(), [root]
        while queue :
            result.append([ x.val for x in queue ])
            queue = [ child for parent in queue for child in parent.children ]
        
        return result
            

#     def levelOrder(self, root: 'Node') -> List[List[int]]:
#         if not root :
#             return list()
        
#         queue, next_queue = [root], []
#         result = list()
#         level = 0
#         while queue or next_queue :
#             if not queue :
#                 queue, next_queue = next_queue, queue
#                 level += 1
#             now = queue.pop(0)
#             if len(result) == level :
#                 result.append([now.val])
#             else :
#                 result[level].append(now.val)
#             if now.children :
#                 next_queue.extend(now.children)
#         return result
