class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        
        while end - start > 1 :
            t = (start + end) // 2
            if nums[t] < target : start = t
            elif nums[t] > target : end = t
            else : return t
        
        if nums[end] == target : return end
        elif nums[start] == target : return start
        else : return -1
    
    # if not binary search
    # def search(self, nums: List[int], target: int) -> int:
    #     try :
    #         return nums.index(target)
    #     except ValueError :
    #         return -1
