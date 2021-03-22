class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increased = decreased = True
        for i in range(1, len(A)) :
            increased = increased and A[i-1] <= A[i]
            decreased = decreased and A[i-1] >= A[i]
        return increased or decreased
