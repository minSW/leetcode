class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r :
            mid = (l+r) // 2
            
            for i in (l, mid, r) :
                if target == nums[i] : return i
            
            if target < nums[mid] :
                if target < nums[l] < nums[mid] :
                    l = mid + 1
                else :
                    r = mid
            else :
                if nums[mid] <= nums[l] <= target :
                    r = mid
                else :
                    l = mid + 1
        
        return -1 if nums[l] != target else l
