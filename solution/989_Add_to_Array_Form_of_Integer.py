class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        i = len(num)-1
        while k or carry :
            if i < 0 :
                num.insert(0, k % 10 + carry)
                i = 0
            else :
                num[i] += k % 10 + carry
            carry = 0
            if num[i] >= 10 :
                carry = 1
                num[i] -= 10
            k //= 10
            i -= 1
        return num
