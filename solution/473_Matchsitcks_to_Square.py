class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n, sum_sides = len(matchsticks), sum(matchsticks)
        
        if sum_sides % 4 != 0 :
            return False
        
        target = [sum_sides // 4] * 4
        matchsticks.sort(reverse=True)
        
        if matchsticks[0] > sum_sides :  
            return False
        
        def dfs(idx: int) :
            if idx == n : return sum(target) == 0
            
            stick = matchsticks[idx]
            for i in range(4) :
                if target[i] >= stick :
                    target[i] -= stick
                    if dfs(idx+1) : return True
                    target[i] += stick
            
            return False
        
        return dfs(0)
