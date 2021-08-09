class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def getIndex(c: str) -> int:
            return ord(c) - ord('a')
        
        n = len(s1)
        counter1, counter2 = [0] * 26, [0] * 26
        
        for c in s1 :
            counter1[getIndex(c)] += 1
        for c in s2[:n] :
            counter2[getIndex(c)] += 1
        
        for i in range(n, len(s2)) :
            if counter1 == counter2 :
                break
            counter2[getIndex(s2[i])] += 1
            counter2[getIndex(s2[i-n])] -= 1
        
        return counter1 == counter2
