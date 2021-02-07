class Solution:
    def freqAlphabets(self, s: str) -> str:
        # chr[97] = 'a'
        result = list()
        i = 0
        while i < len(s) :
            if i + 2 < len(s) and s[i+2] == '#' :
                result.append(chr(int(s[i:i+2]) + 96))
                i += 3
            else :
                result.append(chr(int(s[i]) + 96))
                i += 1
        
        return "".join(result)
