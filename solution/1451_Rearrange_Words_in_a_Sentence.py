class Solution:
    def arrangeWords(self, text: str) -> str:
        position = sorted([ (i, w) for i, w in enumerate(text.lower().split(" ")) ], key=lambda x: (len(x[1]), x[0]))
        res = " ".join([ word for i, word in position ])
        return res[0].upper() + res[1:] # capitalize()
