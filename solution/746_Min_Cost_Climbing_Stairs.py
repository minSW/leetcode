class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)) :
            cost[i] += min(cost[i-2], cost[i-1])
        return min(cost[-1], cost[-2])
