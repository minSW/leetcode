class Solution:
    def isArmstrong(self, N: int) -> bool:
        k, result = len(str(N)), 0
        for i in str(N) :
            result += pow(int(i), k)
        return result == N
