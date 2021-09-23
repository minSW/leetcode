class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024 # 2 ** 10
        count[0] = 1
        res, mask = 0, 0
        
        for w in word :
            letter = 1 << ord(w) - ord('a') # 0000000000 = 'j'...'a'
            mask ^= letter # mask[letter_index] : letter count is even => 0, odd => 1
            
            res += count[mask] # all is even
            res += sum([ count[mask ^ (1 << i)] for i in range(10) ]) # 'a' ~ 'j' is odd
            count[mask] += 1
        
        return res
