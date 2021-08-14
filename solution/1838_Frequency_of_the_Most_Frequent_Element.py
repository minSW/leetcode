class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, acc = 0, k
        
        for right, y in enumerate(nums) :
            if acc + y < self.getX(left, right) * y : # sliding window
                acc -= nums[left]
                left += 1
            acc += nums[right]
        
        return self.getX(left, right) 

    def getX(self, start:int, end: int) -> int :
        return end - start + 1

