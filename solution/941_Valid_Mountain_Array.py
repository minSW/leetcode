class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        top = False
        for i in range(len(arr) - 1) :
            if arr[i] == arr[i+1] or (arr[i] < arr[i+1] and top):
                return False
            elif arr[i] > arr[i+1] :
                if i == 0 : return False
                top = True
        return top
