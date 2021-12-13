class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def timeToVisitTwoPints(index: int) -> int :
            p1, p2 = points[index], points[index+1]
            return max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))
        
        return sum([ timeToVisitTwoPints(i) for i in range(len(points)-1) ])
