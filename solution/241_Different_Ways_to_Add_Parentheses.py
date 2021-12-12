class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        mem = dict()
        
        def compute(a:int, b:int, op: str) -> int :
            if op == "*" : return a * b
            elif op == "+" : return a + b
            elif op == "-" : return a - b
        
        def dfs(exp: str) -> List[int] :
            if exp.isdigit() :
                mem[exp] = [int(exp)]
            elif not exp in mem : 
                res = []
                for i, c in enumerate(exp) :
                    if not c.isdigit() :
                        left, right = dfs(exp[:i]), dfs(exp[i+1:])
                        res += [ compute(l, r, c) for l in left for r in right ]
                mem[exp] = res
            
            return mem[exp]
        
        return dfs(expression)
