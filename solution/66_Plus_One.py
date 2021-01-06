class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join([str(s) for s in digits]))
        next = num + 1
        next_digits = [int(c) for c in str(next)]

        if num == 0 :
            next_digits = [0] * (len(digits) - len(next_digits)) + next_digits

        return next_digits
