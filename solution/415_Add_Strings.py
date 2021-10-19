class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry, n, m = 0, len(num1), len(num2)
        res = []
        
        for i in range(max(n, m)) :
            if i < n :
                carry += int(num1[-1 * i - 1])
            if i < m :
                carry += int(num2[-1 * i - 1])
            res.append(str(carry % 10))
            carry = carry // 10
        
        if carry :
            res.append(str(carry))
        
        return "".join(res[::-1])
