class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        target = 0
        for i in range(len(nums)) :
            if nums[target] == 0 and nums[i] != 0 :
                nums[target], nums[i] = nums[i], nums[target]
            if nums[target] != 0 :
                target += 1

    # def moveZeroes(self, nums: List[int]) -> None:
    #     i, n = 0, len(nums)
    #     while i < len(nums) :
    #         if nums[i] == 0 :
    #             del nums[i]
    #         else :
    #             i += 1
    #     nums.extend([0] * (n - i))
