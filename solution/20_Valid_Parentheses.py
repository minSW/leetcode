class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        pair = {')': '(', '}':'{', ']':'['}
        
        result = True
        for i in s :
            if i in pair:
                if len(stack) > 0 and pair[i] == stack[-1]:
                    del stack[-1]
                else:
                    result = False
                    break
            else :
                stack.append(i)
        
        if stack :
            result = False
        
        return result
        
