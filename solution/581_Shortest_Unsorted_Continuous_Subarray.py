class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        unsorted = keep = 0
        for ori, sort in zip(nums, sorted(nums)) :
            if ori != sort :
                unsorted += keep + 1
                keep = 0
            elif unsorted > 0 :
                keep += 1
        return unsorted
