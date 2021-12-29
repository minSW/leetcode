class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = dict()
        
        def getWinnerScore(start: int, end: int) :
            if start == end :
                return nums[start]
            
            if not (start, end) in dp :
                dp[start, end] = max(nums[start] - getWinnerScore(start+1, end), nums[end] - getWinnerScore(start, end-1))
            
            return dp[start, end]
        
        return getWinnerScore(0, len(nums)-1) >= 0
