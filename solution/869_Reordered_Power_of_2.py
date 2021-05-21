class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = sorted(str(n))
        minimum, maximum = int("".join(digits)), int("".join(digits[::-1]))
        now = 1
        while now * 2 <= minimum :
            now *= 2
        
        while now <= maximum :
            if sorted(str(now)) == digits :
                return True
            now *= 2
        return False
