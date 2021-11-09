class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        group = dict()
        
        def findGroups(node: int, group_num: int) -> bool :
            if not node in group :
                group[node] = group_num
            
            res = True           
            
            for target in graph[node] :
                if not target in group :
                    res = res and findGroups(target, group_num ^ 1)
                elif group[target] == group[node] :
                    return False
            
            return res
        
        return all([ findGroups(i, 0) for i in range(len(graph)) ])

    
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         setA, setB = set(), set()
#         edges = []
        
#         for u, nodes in enumerate(graph) :
#             if nodes and not setA and not setB :
#                 setA.add(u)
#                 setB = set(nodes)
#             elif u in setA :
#                 for node in nodes :
#                     if node in setA : return False
#                     setB.add(node)
#             elif u in setB :
#                 for node in nodes :
#                     if node in setB : return False
#                     setA.add(node)
#             else :
#                 for node in nodes :
#                     edges.append((u, node))
        
#         for x, y in edges :
#             if (x in setA and y in setA) or (x in setB and y in setB) :
#                 return False
#             else :
#                 if x in setA : setB.add(y)
#                 elif y in setA : setB.add(x)
#                 elif x in setB : setA.add(y)
#                 else: setA.add(x)
        
#         return True
