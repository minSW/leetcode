class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_set = dict()
        n = len(nums)
        for i in nums :
            if i in nums_set :
                nums_set[i] += 1
            else :
                nums_set[i] = 1
            
            if nums_set[i] > n / 2 :
                return i

    # # solution
    # def majorityElement(self, nums: List[int]) -> int:
    #     return sorted(nums)[len(nums) // 2]
