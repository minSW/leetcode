class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_list = [0] * len(nums)
        minimum = 10 ** 9
        
        for i, x in enumerate(nums) :
            minimum = min(x, minimum)
            min_list[i] = minimum
        
        stack = []
        for j in range(len(nums)-1, -1, -1) :
            while stack and stack[-1] <= min_list[j] :
                stack.pop()
            
            if stack and min_list[j] < stack[-1] < nums[j] :
                return True
            elif nums[j] > min_list[j] :
                stack.append(nums[j])
        
        return False 
