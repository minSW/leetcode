class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        decreased = False
        
        for i in range(n-1) :
            if nums[i] > nums[i+1] :
                if decreased : 
                    return False
                elif not i in (0, n-2) and nums[i-1] > nums[i+1] and nums[i] > nums[i+2] :
                    return False
                
                decreased = True
        
        return True
