class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res, odd = 0, []
        start = -1
        
        for i in range(len(nums)+1) :
            if i == len(nums) or nums[i] & 1 :
                if len(odd) == k :
                    res += (odd[0] - start) * (i - odd[-1])
                    start = odd.pop(0)
                odd.append(i)
        
        return res
