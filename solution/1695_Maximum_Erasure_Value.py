class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = max_score = 0
        i = start = 0
        unique = set()
        
        while i < len(nums) :
            if nums[i] in unique :
                unique.remove(nums[start])
                score -= nums[start]
                start += 1
            else :
                unique.add(nums[i])
                score += nums[i]
                i += 1
            max_score = max(max_score, score)
        
        return max_score
