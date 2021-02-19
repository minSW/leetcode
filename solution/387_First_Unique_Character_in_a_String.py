class Solution:
    def firstUniqChar(self, s: str) -> int:
        candidate, checked = list(), set()
        
        for i in s :
            if i in candidate :
                candidate.remove(i)
                checked.add(i)
            elif not i in checked :
                candidate.append(i)
        
        if not candidate :
            return -1
        else :
            return s.find(candidate[0])
