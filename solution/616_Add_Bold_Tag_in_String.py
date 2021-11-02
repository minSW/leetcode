class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        res, block = "", False
        
        n = len(s)
        highlight = [0] * n
        
        prefix = collections.defaultdict(list)
        for word in words :
            prefix[word[0]].append(word)
        
        for i, x in enumerate(s) :
            for word in prefix[x] :
                if i + len(word) - 1 < n and s[i:i+len(word)] == word :
                    for j in range(len(word)) :
                        highlight[i+j] = 1
        
        for i in range(n) :
            if highlight[i] and not block :
                res += "<b>"
                block = True
            elif not highlight[i] and block :
                res += "</b>"
                block = False
            res += s[i]
        
        return res if not block else res + "</b>"
