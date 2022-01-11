import collections

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        res = active_frog = 0
        
        croak = { x : i for i, x in enumerate("croak") }
        croak_cnt = [0, 0, 0, 0, 0]
        
        for x in croakOfFrogs :
            i = croak[x]
            croak_cnt[i] += 1
            
            if i == 0 :
                active_frog += 1
                res = max(res, active_frog)
            else :
                croak_cnt[i-1] -= 1
                if croak_cnt[i-1] < 0 :
                    return -1
                elif i == 4 :
                    active_frog -= 1
        
        return res if not active_frog else -1
