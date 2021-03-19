class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(B) - sum(A)) // 2
        B_set = set(B)
        for a in A :
            if a + diff in B_set :
                return [a, a+diff]

