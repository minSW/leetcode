class Solution:
    def calculate(self, s: str) -> int:
        res = []
        op, isDigit = "", False
        
        for i, c in enumerate(s) :
            if c.isdigit() :
                if res and isDigit :
                    res[-1] = res[-1] * 10 + int(c)
                else :
                    res.append(int(c))
                    isDigit = True
            if c in ["+", "-", "/", "*"] or i == len(s) - 1 :
                if op == "-" :
                    res[-1] *= -1
                elif op == "*" :
                    pop = res.pop()
                    res[-1] *= pop
                elif op == "/" :
                    pop = res.pop()
                    const = -1 if res[-1] < 0 else 1
                    res[-1] = const * (abs(res[-1]) // pop)
                op = c
                isDigit = False
        
        return sum(res)
    `
