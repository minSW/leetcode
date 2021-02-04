class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums_sum = 0
        result = []
        for i in nums :
            nums_sum += i
            result.append(nums_sum)
        return result
