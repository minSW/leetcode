class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        checked = dict()
        for i in range(0, len(nums)):
            if nums[i] in checked :
                distance = min(checked[nums[i]][1], i - checked[nums[i]][0]) if (checked[nums[i]][1] != 0) else i - checked[nums[i]][0]
                checked[nums[i]] = (i, distance)
            else :
                checked[nums[i]] = (i, 0)
        
        result = False
        
        for value in checked.values():
            if value[1] > k :
                result = False
                break
            elif value[1] != 0:
                result = True
                
        return result
