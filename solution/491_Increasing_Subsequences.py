class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backTracking(index: int, path: List[int]) -> List[List[int]]:
            res, checked = list(), set()
            if len(path) >= 2 :
                res.append(path)
            
            for i in range(index, len(nums)) :
                if (path and path[-1] > nums[i]) or nums[i] in checked :
                    continue
                checked.add(nums[i])
                res.extend(backTracking(i+1, path+[nums[i]]))
            
            return res
        
        return backTracking(0, []) 

