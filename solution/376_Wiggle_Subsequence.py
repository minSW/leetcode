class Solution:
    
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pos, neg = 1, 1
        for i in range(len(nums)-1) :
            if nums[i] == nums[i+1] :
                continue
            elif nums[i] > nums[i+1] :
                neg = pos + 1
            else :
                pos = neg + 1
        return max(pos, neg)
