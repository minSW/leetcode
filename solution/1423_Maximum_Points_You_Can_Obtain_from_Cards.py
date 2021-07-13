class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        t = len(cardPoints) - k
        if not t :
            return sum(cardPoints)
        
        min_sum = now = sum(cardPoints[:t])
        for i in range(1, k+1) :
            now = now + cardPoints[i+t-1] - cardPoints[i-1]
            min_sum = min(min_sum, now)
        return sum(cardPoints) - min_sum
