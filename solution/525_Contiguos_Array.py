class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = now = 0
        min_dict = { 0 : -1 }
        
        for i in range(len(nums)) :
            if nums[i] == 0 : now -= 1
            else : now += 1
            
            if now in min_dict :
                max_len = max(max_len, i - min_dict[now])
            else :
                min_dict[now] = i
        
        return max_len
