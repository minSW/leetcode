class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        distance = dict()
        for x in arr:
            if x - difference in distance :
                distance[x] = distance[x - difference] + 1
            else :
                distance[x] = 1
        return max(distance.values())
