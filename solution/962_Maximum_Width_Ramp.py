class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res, min_index = 0, len(nums)
        ramp = collections.defaultdict(list)
        
        for i, x in enumerate(nums) :
            ramp[x].append(i)
        
        for k, v in sorted(ramp.items(), key=lambda x:x[0]) :
            min_index = min(min_index, v[0])
            res = max(res, v[-1] - min_index)
        
        return res
