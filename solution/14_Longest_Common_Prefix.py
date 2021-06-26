class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        for s in strs[1:] :
            common = ""
            for p, t in zip(common_prefix, s) :
                if p == t : common += p
                else : break
            common_prefix = common
        return common_prefix
