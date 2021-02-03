class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n) :
            nums.insert(1+i*2, nums[n+i*2])
        return nums[:n*2]
