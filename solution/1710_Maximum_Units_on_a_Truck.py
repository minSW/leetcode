class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        for num, units in sorted(boxTypes, key=lambda x:(-x[1],-x[0])) :
            if not truckSize : 
                break
            k = min(num, truckSize)
            res += k * units
            truckSize -= k
        
        return res
