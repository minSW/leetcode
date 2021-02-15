class Solution:
    def maxPower(self, s: str) -> int:
        now, now_len, max_len = "", 1, 1
        
        for i in s :
            if now != i :
                max_len = max(max_len, now_len)
                now, now_len = i, 1
            else :
                now_len += 1
        return max(max_len, now_len)
