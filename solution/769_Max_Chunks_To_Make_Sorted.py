class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count, ele_max = 0, 0
        
        for i, x in enumerate(arr) :
            ele_max = max(i, x, ele_max)
            if ele_max == i :
                count += 1
        return count
