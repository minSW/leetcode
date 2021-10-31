class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        return ([ i for i in range(len(arr)) if i == arr[i] ] + [-1])[0]
