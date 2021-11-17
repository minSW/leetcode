class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1 :
            return [nums]
        
        res, checked = list(), set()
        
        for i, x in enumerate(nums) :
            if not x in checked :
                checked.add(x)
                for sub in self.permuteUnique(nums[:i]+nums[i+1:]) :
                    res.append([nums[i]] + sub)
        
        return res
