class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        max_wpi = score = 0
        res = {}
        
        for i, h in enumerate(hours) :
            score = score + 1 if h > 8 else score - 1
            if score > 0 :
                max_wpi = i + 1 # 0 to i
            if not score in res :
                res[score] = i
            if score - 1 in res :
                max_wpi = max(max_wpi, i - res[score - 1]) # (res[score] - res[score-1]) => positive score (+1) maximum length
        
        return max_wpi
