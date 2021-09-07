class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        count, checked = 0, {}
        end_index, now = -1, 0
        
        for i, x in enumerate(nums) :
            now += x
            if (now - target in checked and checked[now-target] >= end_index) or (now == target and end_index == -1) :
                count += 1
                end_index = i
            checked[now] = i
        return count
