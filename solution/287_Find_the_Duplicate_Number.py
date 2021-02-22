class Solution:
    # Floyd's Cycle Detection Algorithm
    def findDuplicate(self, nums: List[int]) -> int:
        head, slow, fast = 0, nums[0], nums[nums[0]]
        while slow != fast :
            slow, fast = nums[slow], nums[nums[fast]]
        while head != slow :
            head, slow = nums[head], nums[slow]
        return head
    
    # Simple Solution (set() use)
    # def findDuplicate(self, nums: List[int]) -> int:
    #     nums_set = set()
    #     for i in nums :
    #         if i in nums_set :
    #             nums_set.remove(i)
    #         else :
    #             return i
