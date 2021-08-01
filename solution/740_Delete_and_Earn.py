class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = [0] * 10001
        for x in nums :
            points[x] += x
        
        prev, curr = 0, 0
        for p in points :
            prev, curr = curr, max(prev+p, curr)
        
        return curr
