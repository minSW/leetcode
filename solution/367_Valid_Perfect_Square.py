class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 0, num
        
        while start <= end :
            mid = (start + end) // 2
            if mid * mid < num :
                start = mid + 1
            elif mid * mid > num :
                end = mid - 1
            else :
                return True
        
        return False
