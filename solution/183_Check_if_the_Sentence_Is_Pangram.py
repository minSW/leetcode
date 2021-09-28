class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

    # def checkIfPangram(self, sentence: str) -> bool:
    #     if len(sentence) < 26 :
    #         return False
    #     count = [0] * 26
    #     for x in sentence :
    #         count[ord(x)-ord('a')] += 1
    #     return all(count)
