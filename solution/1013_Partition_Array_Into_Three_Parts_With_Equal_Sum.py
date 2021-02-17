class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        all_sum = sum(arr)
        if all_sum % 3 != 0 :
            return False
        
        now, count = 0, 0
        
        for a in range(len(arr)-1) :
            if count == 2 :
                break
            now += arr[a]
            if now == all_sum // 3 :
                count += 1
                now = 0
        
        return count == 2
