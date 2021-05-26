class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = Counter((s1 + " " + s2).split(" "))
        return [ x for x in c1 if c1[x] == 1 ]
