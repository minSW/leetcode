class Solution:
    # Use XOR
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for i in s + t:
            res ^= ord(i)
        
        return chr(res)
        
    # def findTheDifference(self, s: str, t: str) -> str:
    #     s_dict = { x : s.count(x) for x in set(s) }
    #     for i in t :
    #         if not i in s_dict or s_dict[i] == 0 :
    #             return i
    #         else :
    #             s_dict[i] -= 1
