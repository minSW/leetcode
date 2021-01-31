class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1
        
        for i in range(len(arr) - 1, -1, -1) :
            target, arr[i] = arr[i], maximum
            if target > maximum :
                maximum = target
        
        return arr
