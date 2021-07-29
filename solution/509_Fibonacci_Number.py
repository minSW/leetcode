class Solution:
    def fib(self, n: int) -> int:
        mem = [ 0, 1 ]
        if n > 1 :
            for i in range(2, n+1) :
                mem.append(mem[i-1] + mem[i-2])
        return mem[n]
