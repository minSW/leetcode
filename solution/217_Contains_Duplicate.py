class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     checked = set()
    #     for n in nums:
    #         if n in checked:
    #             return True
    #         else :
    #             checked.add(n)
    #     return False
