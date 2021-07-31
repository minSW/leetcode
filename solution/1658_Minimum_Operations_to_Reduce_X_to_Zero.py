class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n, target, now = len(nums), sum(nums) - x, nums[0]
        
        if not target :
            return n
        
        start = i = 0
        res = -1
        
        while i < n :
            if start > i or now < target :
                i += 1
                if i < n :
                    now += nums[i]
            else :
                if now == target :
                    res = min(res, n-(i-start+1)) if res > 0 else n-(i-start+1)
                now -= nums[start]
                start += 1
        
        return res

