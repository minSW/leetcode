class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        now, count, bound = -1, 0, len(arr) * 0.25
        
        for i in arr :
            if now == i :
                count += 1
            else :
                now = i
                count = 1
            
            if count > bound :
                break
        
        return now
