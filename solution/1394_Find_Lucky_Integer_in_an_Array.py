class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        cnt = 1
        
        for i in range(1, len(arr)) :
            if arr[i] == arr[i-1] :
                cnt += 1
            elif arr[i-1] == cnt :
                return cnt
            else :
                cnt = 1
        
        return cnt if arr[-1] == cnt else -1
