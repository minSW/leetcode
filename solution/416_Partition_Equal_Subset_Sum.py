class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        subsets_sum = set()
        
        if target % 2 == 1 : 
            return False
        else :
            target //= 2
        
        for x in sorted(nums) :
            if not subsets_sum :
                subsets_sum.add(x)
            else :
                subsets_sum.update([ e + x for e in subsets_sum ])
            
            if target in subsets_sum :
                return True
        
        return False
