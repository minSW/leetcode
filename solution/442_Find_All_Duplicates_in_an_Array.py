class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums :
            if nums[abs(x)-1] < 0 :
                res.append(abs(x))
            else :
                nums[abs(x)-1] *= -1
        return res

    # def findDuplicates(self, nums: List[int]) -> List[int]:
    #     nums.sort()
    #     now, res = 1, []
    #     for x in nums :
    #         if now == x : now += 1
    #         elif now < x : now = x + 1
    #         else :
    #             res.append(x)
    #             now = x + 1
    #     return res
