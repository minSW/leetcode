class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        B = [ 0 for _ in range(len(A)) ]
        even, odd = 0, 1
        for i in A :
            if i % 2 == 0:
                B[even] = i
                even += 2
            else :
                B[odd] = i
                odd += 2
        return B
