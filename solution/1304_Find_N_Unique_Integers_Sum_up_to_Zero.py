class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [i for i in range(1, n//2+1) ]
        result.extend([-i for i in result])
        if n % 2 == 1 :
            result.append(0)
        return result
