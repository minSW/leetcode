class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        gradient = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]) if coordinates[1][0] - coordinates[0][0] else 10 ^ 5 # inf
        
        for i in range(2, len(coordinates)) :
            if coordinates[i][0] - coordinates[i-1][0] == 0 :
                if gradient != 10 ^ 5 : 
                    return False
            elif (coordinates[i][1] - coordinates[i-1][1]) / (coordinates[i][0] - coordinates[i-1][0]) != gradient :
                return False
        
        return True
