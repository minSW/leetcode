class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        minimum = [-10001]
        for x in nums :
            if minimum[-1] < x :
                minimum.append(x)
            else :
                for j in range(len(minimum)-2, -1, -1) :
                    if minimum[j] < x :
                        minimum[j+1] = min(minimum[j+1], x)
                        break
        return len(minimum) - 1
