class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod, res = {nums[0] : 0}, nums[0]
        
        for i in range(1, len(nums)) :
            if nums[i] + nums[i-1] == 0 :
                return True
            
            res = (res + nums[i]) % k
            if res == 0 or res in mod and i - mod[res] > 1 :
                return True
            elif not res in mod :
                mod[res] = i
        
        return False
