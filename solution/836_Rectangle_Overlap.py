class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def isLinear(rec: List[int]) -> bool :
            return rec[0] == rec[2] or rec[1] == rec[3]
        
        if isLinear(rec1) or isLinear(rec2) : 
            return False
        return rec2[0] < rec1[2] and rec2[1] < rec1[3] and rec2[2] > rec1[0] and rec2[3] > rec1[1] 
