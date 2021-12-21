class Solution:
    # Topological Sorting Solution
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges :
            return [0]

        nodes = collections.defaultdict(set)
        
        for u, v in edges :
            nodes[u].add(v)
            nodes[v].add(u)
        
        stack = [ i for i in range(n) if len(nodes[i]) == 1 ]
        next_stack = []
        
        while n > len(stack) :
            n -= len(stack)
            
            for u in stack :
                v = nodes[u].pop()
                nodes[v].remove(u)
                
                if len(nodes[v]) == 1 :
                    next_stack.append(v)
            
            stack, next_stack = next_stack, []
        
        return stack
