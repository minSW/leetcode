class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusty_count = [0] * (n + 1)
        for a, b in trust :
            trusty_count[a] -= 1
            trusty_count[b] += 1
        
        judge = [ i for i in range(1, n+1) if trusty_count[i] == n - 1 ]
        return judge[0] if len(judge) == 1 else -1
