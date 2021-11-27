class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits, index = [ int(x) for x in str(n) ], dict()
        N = len(digits)
        
        for i, x in enumerate(digits[:-1]) :
            if not x in index :
                index[x] = i
            
            if digits[i] > digits[i+1] :
                divisor = 10 ** (N-1-index[x])
                return n // divisor * divisor - 1
        
        return n
