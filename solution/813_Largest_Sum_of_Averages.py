class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n, dp = len(nums), dict()
        
        def getAvg(start:int, end:int) -> float :
            return sum(nums[start:end]) / (end-start)
        
        def dfs(index: int, t:int) -> float :
            if not (index, t) in dp :
                if t == 1 :
                    dp[(index, t)] = getAvg(index, n)
                elif t == (n-index) :
                    dp[(index, t)] = sum(nums[index:])
                else :
                    dp[(index, t)] = max([ getAvg(index, i) + dfs(i, t-1) for i in range(index+1, n-t+2) ])
            return dp[(index, t)]
        
        return dfs(0, k)
