class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res, mask, mask_dict = 0, 0, { 0 : -1 }
        vowel = "aeiou" # => 00000 (uoiea) xor mask
        
        for i, c in enumerate(s) :
            mask ^= 1 << vowel.find(c) if c in vowel else 0
            if not mask in mask_dict :
                mask_dict[mask] = i
            else :
                res = max(i - mask_dict[mask], res)
        
        return res
