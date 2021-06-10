class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        now = 1
        for a in arr :
            if now == a :
                now += 1
            elif a - now < k :
                k -= a - now
                now = a + 1
            else :
                break
        return now + k - 1
