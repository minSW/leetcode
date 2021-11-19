class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        inf = 10 ** 5
        
        def getGradient(point1: List[int], point2: List[int]) -> int :
            x1, y1 = point1
            x2, y2 = point2
            return (y2 - y1) / (x2 - x1) if x2 - x1 else inf
        
        gradient = getGradient(coordinates[0], coordinates[1])
        return not any([ gradient != getGradient(coordinates[0], point) for point in coordinates[2:] ])
