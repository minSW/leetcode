class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [0, 0]
        nums.sort()
        
        # [ 중복된거 , 빠진거 ]
        origin = set(i for i in range (1, len(nums)+1))
        
        for i in range (len(nums)) :
            if nums[i] in origin :
                origin.remove(nums[i])
            else :
                result[0] = nums[i]
        result[1] = list(origin)[0]
        return result
    
    # # solution
    # def findErrorNums(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     s = n*(n+1)//2
    #     miss = s - sum(set(nums))
    #     duplicate = sum(nums) + miss - s
    #     return [duplicate, miss]
