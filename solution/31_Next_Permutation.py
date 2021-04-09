class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = n = len(nums)
        
        for i in range(n-1) :
            if nums[i] < nums[i+1] :
                pivot = i
        
        if pivot == n :
            nums.reverse()
        
        for j in range(n-1, pivot, -1) :
            if nums[pivot] < nums[j] :
                nums[pivot], nums[j] = nums[j], nums[pivot]
                nums[pivot+1:] = reversed(nums[pivot+1:])
                break

