class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        diff = 0
        
        for num in nums :
            diff ^= num
        
        last_bit = diff & (-diff)
        
        for num in nums :
            if num & last_bit :
                res[0] ^= num
            else :
                res[1] ^= num
        return res
    
    # another solution - O(n) O(1)
    # def singleNumber(self, nums: List[int]) -> List[int]:
    #     nums.sort()
    #     res = []
    #     i = 0
    #     while i < len(nums) :
    #         if i == len(nums) - 1 or nums[i] != nums[i+1]:
    #             res.append(nums[i])
    #             i += 1
    #         else :
    #             i += 2
    #     return res

