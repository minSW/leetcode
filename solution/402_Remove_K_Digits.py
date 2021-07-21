class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for x in num :
            while stack and stack[-1] > x :
                if not k :
                    break
                stack.pop()
                k -= 1
            stack.append(x)
        
        if k :
            stack = stack[:-k]
        
        return "".join(stack).lstrip("0") or "0"
