class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        return [ i + extraCandies >= maximum for i in candies ]
