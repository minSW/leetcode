import collections

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connected = collections.defaultdict(set)
        
        for a, b in edges :
            connected[a].add(b)
            connected[b].add(a)
        
        can_removed = True
        while can_removed :
            can_removed = False
            for k, v in connected.items() :
                if len(v) == 1 :
                    connected[v.pop()].remove(k)
                    can_removed = True
        
        for e in reversed(edges) :
            if connected[e[0]] and connected[e[1]] :
                return e
