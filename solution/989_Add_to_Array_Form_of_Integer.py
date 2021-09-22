class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry, i = 0, len(num) - 1
        
        while k or carry :
            if i < 0 :
                num.insert(0, 0)
                i = 0
            num[i] += k % 10 + carry
            carry, k = 0, k // 10
            if num[i] >= 10 :
                carry, num[i] = 1, num[i] % 10
            i -= 1
        
        return num
