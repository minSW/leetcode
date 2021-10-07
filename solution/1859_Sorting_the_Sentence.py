class Solution:
    def sortSentence(self, s: str) -> str:
        sorted_words = sorted([word[-1]+word[:-1] for word in s.split(" ")])
        return " ".join([x[1:] for x in sorted_words])
