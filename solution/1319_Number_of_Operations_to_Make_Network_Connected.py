class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1 :
            return -1
        G, visited = [ set() for i in range(n) ], [ 0 for _ in range(n) ]
        
        for x in connections :
            G[x[0]].add(x[1])
            G[x[1]].add(x[0])
        
        def dfs(i) :
            if visited[i] :
                return 0
            visited[i] = 1
            for j in G[i] :
                dfs(j)
            return 1
        
        return sum(dfs(i) for i in range(n)) - 1
