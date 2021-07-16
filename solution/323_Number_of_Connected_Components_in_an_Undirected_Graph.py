class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = { i : list() for i in range(n) }
        checked = [0] * n
        
        for a, b in edges :
            nodes[a].append(b)
            nodes[b].append(a)
        
        def dfs(i : int) :
            if checked[i] : 
                return False
            
            checked[i] = 1
            for k in nodes[i] :
                dfs(k)
            return True
        
        return len([ i for i in range(n) if dfs(i) ])
