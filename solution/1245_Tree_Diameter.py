class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        nodes = collections.defaultdict(list)
        res = []
        
        for u, v in edges :
            nodes[u].append(v)
            nodes[v].append(u)
        
        def dfs(node: int, prev: int) -> int :
            distances = sorted([0, 0] + [ dfs(x, node) for x in nodes[node] if x != prev ], reverse=True)
            res.append(sum((distances)[:2]))
            return distances[0] + 1
        
        dfs(0, 0)
        
        return max(res)
    
    # Time Limit Exceeded Solution
#     def treeDiameter(self, edges: List[List[int]]) -> int:
#         nodes = collections.defaultdict(list)
        
#         for u, v in edges :
#             nodes[u].append(v)
#             nodes[v].append(u)
        
#         def dfs(node: int, path: Set[int]) -> int :
#             path.add(node)
#             return max([0] + [ dfs(x, path) + 1 for x in nodes[node] if not x in path ])
        
#         return max([0] + [ dfs(node, set()) for node in nodes.keys() if len(nodes[node]) == 1 ])
