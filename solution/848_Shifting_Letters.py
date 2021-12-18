class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        tmp = sum(shifts)
        
        for i in range(len(shifts)) :
            shifts[i], tmp = tmp, tmp - shifts[i]
        
        return "".join([ chr(ord('a') + (ord(c) - ord('a') + shift) % 26) for c, shift in zip(s, shifts) ])
