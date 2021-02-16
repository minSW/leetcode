class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0 or rowIndex == 1:
            return [1] * (rowIndex + 1)
        
        result, prev = [1], self.getRow(rowIndex - 1)
        for i in range(len(prev) - 1) :
            result.append(prev[i] + prev[i+1])
        return result + [1]

