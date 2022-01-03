class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack, res = [], [0] * n
        
        for i in range(n) :
            while stack and temperatures[stack[-1]] < temperatures[i] :
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        
        return res
