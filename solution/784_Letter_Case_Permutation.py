class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        per = dict()
        
        def getPermutation(index: int) -> List[str]:
            if index == len(s) :
                return [""]
            elif not index in per :
                c = s[index]
                target =  [ c.upper(), c.lower() ] if c.isalpha() else [ c ] 
                per[index] = [ now + tail for tail in getPermutation(index+1) for now in target ]
            return per[index]
        
        return getPermutation(0)
