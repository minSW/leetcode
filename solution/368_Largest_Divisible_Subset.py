class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        
        checked = { i : {nums[i]} for i in range(n) }
        target = [ i for i in range(n) ]
        
        next_target, result = set(), list()
        while target :
            i = target.pop(0)
            for j in target :
                if nums[j] % nums[i] == 0 and i < j :
                    if len(checked[j]) < len(checked[i]) + 1 :
                        checked[j] = {nums[j]} | checked[i]
                    next_target.add(j)
            if not target :
                target, next_target = list(next_target).sort(), set()
        
        return max(checked.values(), key=len)
    
    # def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    #     S = {-1: set()}
    #     for x in sorted(nums) :
    #         S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
    #     return list(max(S.values(), key=len))

