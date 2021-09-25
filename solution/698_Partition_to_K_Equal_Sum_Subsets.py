class Solution:
    # Similar to '#473'
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summation = sum(nums)
        if summation % k != 0 :
            return False
        target = [ summation // k ] * k
        nums.sort(reverse=True)
        
        def dfs(index: int) :
            if index == len(nums) :
                return True
            for i in range(k) :
                if target[i] >= nums[index] :
                    target[i] -= nums[index]
                    if dfs(index+1) :
                        return True
                    target[i] += nums[index]
            return False
        
        return dfs(0)
