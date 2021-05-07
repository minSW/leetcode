class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        abs_minimum = min(y-x for x, y in zip(arr, arr[1:]))
        return [ [x,y] for x, y in zip(arr, arr[1:]) if y-x == abs_minimum ]
