class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B) : return False
        elif not A : return True
        
        for i in range(0, len(A)) :
            if A[:i] in B and A[i:] + A[:i] == B :
                    return True
        return False
    
    # solution
    # def rotateString(self, A: str, B: str) -> bool:
    #     return len(A) == len(B) and B in A + A
