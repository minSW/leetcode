class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        result = cnt = 1
        prev = 0
        
        for i in range(1, len(arr)) :
            now = arr[i] - arr[i-1]
            if now * prev < 0 :
                cnt += 1
            elif now == 0 :
                cnt = 1
            else :
                cnt = 2
            result = max(cnt, result)
            prev = now
        
        return result
