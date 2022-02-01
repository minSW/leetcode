class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n, MAX_COST = len(days), 1000 * 365
        
        cost_map = { costs[i] : x for i, x in enumerate([1, 7, 30]) }
        mem = {}
        
        def dp(index: int) -> int :
            if index >= n :
                return 0
            elif not index in mem :
                res = MAX_COST
                next_index = index
                
                for c, d in cost_map.items() :
                    while next_index < n :
                        if days[index] + d <= days[next_index] : break
                        next_index += 1
                    res = min(res, dp(next_index) + c)
                
                mem[index] = res
            
            return mem[index]
        
        return dp(0)
